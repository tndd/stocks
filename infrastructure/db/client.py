from contextlib import closing
from typing import List

from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import Statement

from common.decorator import count_time
from infrastructure.db.model.common import TableDataset


class PostgresClient(BaseModel):
    database: str
    user: str
    password: str
    host: str
    port: str

    @property
    def engine(self):
        if self._engine is None:
            self._engine = create_engine(
                f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'
            )
        return self._engine

    def store_table_dataset(self, table_ds: TableDataset, is_ignore_key_conflict: bool = True):
        """
        Basically ignore key conflict and store data.
        """
        stmt = table_ds.get_insert_stmt(is_ignore_key_conflict)
        # Execute the statement
        self._execute_stmt(stmt)

    def store_multi_table_datasets(self, table_datasets: List[TableDataset]):
        # TODO
        pass

    def _create_session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return closing(session)

    @count_time
    def _execute_stmt(self, stmt: Statement):
        with self._create_session() as session:
            try:
                session.execute(stmt)
                session.commit()
            except Exception as e:
                session.rollback()
                print(f"Error occurred: {e}")
                raise

    def _execute_multi_stmts(self, stmts: List[Statement]):
        with self._create_session() as session:
            try:
                for stmt in stmts:
                    session.execute(stmt)
                session.commit()
            except Exception as e:
                session.rollback()
                print(f"Error occurred: {e}")
                raise
