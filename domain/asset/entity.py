from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from domain.common.entity.table_record import TableRecord


class Asset(TableRecord):
    id: str
    version: datetime
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
    maintenance_margin_requirement: Optional[str] = None
    attributes: Optional[str] = None
    min_order_size: Optional[float] = None
    min_trade_increment: Optional[float] = None
    price_increment: Optional[float] = None
