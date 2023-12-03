from dataclasses import dataclass
from typing import List

from alpaca.trading.client import TradingClient
from alpaca.trading.enums import AssetClass


@dataclass
class AlpacaApiClient:
    api_key: str
    secret_key: str

    @property
    def trading_client(self) -> TradingClient:
        if self._trading_client is None:
            self._trading_client = TradingClient(
            self.api_key,
            self.secret_key
        )
        return self._trading_client

    def fetch_stock_assets(self) -> List[dict]:
        return self._fetch_assets(asset_class=AssetClass.US_EQUITY)

    def fetch_crypto_assets(self) -> List[dict]:
        return self._fetch_assets(asset_class=AssetClass.CRYPTO)

    def _fetch_assets(self, asset_class: AssetClass) -> List[dict]:
        search_params = self._trading_client.GetAssetsRequest(asset_class=asset_class)
        assets = self._trading_client.get_all_assets(search_params)
        return [asset.model_dump() for asset in assets]