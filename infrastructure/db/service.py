from datetime import datetime
from typing import Any, Dict, List, Optional, Type, get_args, get_origin

from pydantic import BaseModel
from sqlalchemy import (ARRAY, Boolean, Column, DateTime, Float, Integer,
                        PrimaryKeyConstraint, String)
from sqlalchemy.orm import DeclarativeMeta, declarative_base

from infrastructure.db.model.asset import AssetTableMetaData

Base: DeclarativeMeta = declarative_base()

TYPE_MAPPING: Dict[Type, Type] = {
    int: Integer,
    str: String,
    bool: Boolean,
    float: Float,
    datetime: DateTime,
    List[int]: ARRAY(Integer),
    List[str]: ARRAY(String),
    List[bool]: ARRAY(Boolean),
    List[float]: ARRAY(Float),
    List[datetime]: ARRAY(DateTime)
}


def to_sqlalchemy_model(pydantic_model: Type[BaseModel], table_metadata: AssetTableMetaData) -> Type[Base]:
    attrs: Dict[str, Any] = {"__tablename__": table_metadata.TABLE_NAME}

    for field_name, field_type in pydantic_model.__annotations__.items():
        # Check for Option field.
        if get_origin(field_type) is Optional:
            field_type = get_args(field_type)[0]
            nullable: bool = True
        else:
            nullable: bool = False

        # Get column type for SQLAlchemy Base model.
        column_type = TYPE_MAPPING.get(field_type)
        if column_type is None:
            raise ValueError(f"Unexpected field type: {field_type} for field: {field_name}")

        attrs[field_name] = Column(column_type, nullable=nullable)

    # Set primary key.
    attrs['__table_args__'] = (PrimaryKeyConstraint(*table_metadata.PRIMARY_KEYS),)

    return type("SQLAlchemyModel", (Base,), attrs)
