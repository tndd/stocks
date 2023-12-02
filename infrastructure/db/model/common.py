from typing import List

from pydantic import BaseModel

from infrastructure.db.service import Base, to_sqlalchemy_model


class TableMetaData(BaseModel):
    TABLE_NAME: str
    PRIMARY_KEYS: List[str]

    class Config:
        allow_mutation = False


class TableDataset(BaseModel):
    metadata: TableMetaData
    records: List[BaseModel]

    @property
    def columns_definition(self) -> Base:
        """
        Base model for use with SqlAlchemy
        """
        return to_sqlalchemy_model(self.records[0], self.metadata)

    def get_records_as_dict(self) -> List[dict]:
        """
        Get convert records as a list of dictionaries
        """
        return [record.model_dump() for record in self.records]
