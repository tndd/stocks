from concurrent.futures import ProcessPoolExecutor
from contextlib import closing
from typing import List

from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

from infrastructure.db.model.common import TableDataset
from infrastructure.db.adapter import Base


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

    def store_table_dataset(self, table_dataset: TableDataset):
        # TODO
        pass

    def store_multi_table_datasets(self, table_datasets: List[TableDataset]):
        # TODO
        pass

    # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

    def _set_engine(self):
        self.engine = create_engine(
            f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'
        )

    def _create_session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return closing(session)

    def schedule_insert_models(self, model: Base, models: List[dict], session: Session):
        # DUPULICATE KEY WILL BE IGNORED!
        table = model.__table__
        stmt = insert(table).values(models)
        do_nothing_stmt = stmt.on_conflict_do_nothing(index_elements=['id'])
        session.execute(do_nothing_stmt)

    def schedule_parallel_insert_models(self, table_ds: TableDataset, session: Session, n_worker: int = 8):
        # Allcate model for SqlAlchemy operations.
        sql_alchemy_model: Base = table_ds.columns_definition
        # Create table for insert target.
        sql_alchemy_model.metadata.create_all(self.engine)
        # Get converted list dict from table_dataset records.
        records_data: List[dict] = table_ds.get_records_as_dict()
        # Preparation calculation for parallel execution.
        n_chunk = len(records_data) // n_worker
        batches = [records_data[i:i + n_chunk] for i in range(0, len(records_data), n_chunk)]
        # Execute parallel insert.
        with ProcessPoolExecutor(max_workers=n_worker) as executor:
            for batch in batches:
                executor.submit(self.schedule_insert_models, sql_alchemy_model, batch, session)