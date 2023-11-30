from concurrent.futures import ProcessPoolExecutor
from contextlib import closing
from typing import List

from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker


class PostgresClient(BaseModel):
    database: str = "stocks"
    user: str = "postgres"
    password: str = "postgres"
    host: str = "localhost"
    port: str = "5432"
    engine: Engine = None

    def __init__(self, **data):
        super().__init__(**data)
        self._set_engine()

    def _set_engine(self):
        self.engine = create_engine(
            f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'
        )

    def create_session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return closing(session)

    def truncate_insert_models(self, model: Base, data: List[dict]):
        model.metadata.create_all(self.engine)
        with self.create_session() as session:
            session.query(model).delete()
            session.bulk_insert_mappings(model, data)
            session.commit()

    def schedule_insert_models(self, model: Base, models: List[dict], session: Session):
        # Ignore duplicate keys.
        table = model.__table__
        stmt = insert(table).values(models)
        do_nothing_stmt = stmt.on_conflict_do_nothing(index_elements=['id'])
        session.execute(do_nothing_stmt)

    def schedule_parallel_insert_models(self, model: Base, data: List[dict], session: Session, n_worker: int = 8):
        model.metadata.create_all(self.engine)
        n_chunk = len(data) // n_worker
        batches = [data[i:i + n_chunk] for i in range(0, len(data), n_chunk)]
        with ProcessPoolExecutor(max_workers=n_worker) as executor:
            for batch in batches:
                executor.submit(self.schedule_insert_models, model, batch, session)