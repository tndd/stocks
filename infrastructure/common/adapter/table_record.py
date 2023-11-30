from sqlalchemy import Boolean, Column, DateTime, Float, String
from sqlalchemy.schema import PrimaryKeyConstraint

# Define the Asset class
Base: DeclarativeMeta = declarative_base()

# class Asset(Base):
#     __tablename__ = 'assets'

#     id = Column(String)
#     version = Column(DateTime)
#     asset_class = Column(String)
#     exchange = Column(String)
#     symbol = Column(String)
#     name = Column(String)
#     status = Column(String)
#     tradable = Column(Boolean)
#     marginable = Column(Boolean)
#     shortable = Column(Boolean)
#     easy_to_borrow = Column(Boolean)
#     fractionable = Column(Boolean)
#     maintenance_margin_requirement = Column(String)
#     attributes = Column(String)
#     min_order_size = Column(Float)
#     min_trade_increment = Column(Float)
#     price_increment = Column(Float)

#     __table_args__ = (
#         PrimaryKeyConstraint('id', 'version'),
#     )


def _get_column_type(self, value):
        if isinstance(value, str):
            return String
        elif isinstance(value, datetime):
            return DateTime
        elif isinstance(value, bool):
            return Boolean
        elif isinstance(value, float):
            return Float
        else:
            raise ValueError(f"Unsupported type: {type(value)}")

def to_sql_alchemy_model(self, entity: TableModel):
    class SQLAlchemyModel(Base):
        __tablename__ = entity.md_table_name
        __table_args__ = (PrimaryKeyConstraint(*entity.md_primary_keys),)
        # Dynamically add columns based on the properties of the entity
        for key, value in vars(entity).items():
            if not key.startswith("md_"):
                column_type = self._get_column_type(value)
                setattr(SQLAlchemyModel, key, Column(column_type))
    return SQLAlchemyModel