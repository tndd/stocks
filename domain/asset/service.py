from dataclasses import dataclass

from .repository import AssetRepository
from .value import AssetType


@dataclass
class AssetService:
    asset_repositoy: AssetRepository

    def update_assets(self):
        stock_data = self.asset_repositoy.fetch_assets(AssetType.STOCK)
        crypto_data = self.asset_repositoy.fetch_assets(AssetType.CRYPTO)
        self.asset_repositoy.store_assets(stock_data + crypto_data)
