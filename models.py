from sqlalchemy import Boolean, Column, Float, String
from sqlalchemy.orm import DeclarativeMeta, declarative_base

# Define the Asset class
Base: DeclarativeMeta = declarative_base()

class Asset(Base):
    __tablename__ = 'assets'

    id = Column(String, primary_key=True)
    asset_class = Column(String)
    exchange = Column(String)
    symbol = Column(String)
    name = Column(String)
    status = Column(String)
    tradable = Column(Boolean)
    marginable = Column(Boolean)
    shortable = Column(Boolean)
    easy_to_borrow = Column(Boolean)
    fractionable = Column(Boolean)
    maintenance_margin_requirement = Column(String)
    attributes = Column(String)
    min_order_size = Column(Float)
    min_trade_increment = Column(Float)
    price_increment = Column(Float)