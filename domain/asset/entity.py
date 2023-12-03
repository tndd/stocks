from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ValidationError, validator


class Asset(BaseModel):
    id: str
    version: Optional[datetime] = None
    asset_class: str
    exchange: str
    symbol: str
    name: str
    status: str
    tradable: bool
    marginable: bool
    shortable: bool
    easy_to_borrow: bool
    fractionable: bool
    maintenance_margin_requirement: Optional[float] = None
    attributes: Optional[List[str]] = None
    min_order_size: Optional[float] = None
    min_trade_increment: Optional[float] = None
    price_increment: Optional[float] = None