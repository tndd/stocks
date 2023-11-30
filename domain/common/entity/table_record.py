from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class TableRecord(BaseModel):
    """
    This is the base class that represents a single row of records in a table.
    Each subclass represents a table in the database.
    Each attribute of a subclass represents a column of the table.
    """
    pass