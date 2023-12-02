from typing import List

from pydantic import BaseModel
from sqlalchemy.dialects.postgresql import Insert, insert

from infrastructure.db.adapter import Base, to_sqlalchemy_model


class TableMetaData(BaseModel):
    TABLE_NAME: str
    PRIMARY_KEYS: List[str]

    class Config:
        allow_mutation = False


class TableDataset(BaseModel):
    metadata: TableMetaData
    records: List[BaseModel]

    def get_columns_definition(self) -> Base:
        """
        Base model for use with SqlAlchemy
        """
        return to_sqlalchemy_model(self.records[0], self.metadata)

    def get_records_as_dict(self) -> List[dict]:
        """
        Get convert records as a list of dictionaries
        """
        return [record.model_dump() for record in self.records]

    def get_insert_stmt(self, is_ingore_key_conflict: bool = True) -> Insert:
        # SQLAlchemy model for the table
        model = self.get_columns_definition()
        # List of dictionaries representing the records
        records_data = self.get_records_as_dict()
        # Create an insert statement for the table
        stmt = insert(model.__table__).values(records_data)
        # For case of ignore key conflict
        if is_ingore_key_conflict:
            stmt = stmt.on_conflict_do_nothing()
        return stmt
