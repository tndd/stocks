from typing import List

from pydantic import BaseModel


class TableMetaData(BaseModel):
    TABLE_NAME: str
    PRIMARY_KEYS: List[str]

    class Config:
        allow_mutation = False