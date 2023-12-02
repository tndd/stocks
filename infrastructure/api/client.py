from typing import List

from alpaca.trading.client import TradingClient
from alpaca.trading.enums import AssetClass
from alpaca.trading.requests import GetAssetsRequest
from pydantic import BaseModel


class AlpacaApiClient(BaseModel):
    api_key: str
    secret_key: str
    trading_client: TradingClient = None

    def __init__(self, **data):
        super().__init__(**data)
        self._set_trading_client()

    def _set_trading_client(self):
        self.trading_client = TradingClient(self.api_key, self.secret_key)

    def fetch_assets(self, asset_class: AssetClass) -> List[dict]:
        search_params = GetAssetsRequest(asset_class=asset_class)
        assets = self.trading_client.get_all_assets(search_params)
        return [asset.model_dump() for asset in assets]

    def fetch_stock_assets(self) -> List[dict]:
        return self.fetch_assets(asset_class=AssetClass.US_EQUITY)

    def fetch_crypto_assets(self) -> List[dict]:
        return self.fetch_assets(asset_class=AssetClass.CRYPTO)