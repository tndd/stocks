from dataclasses import dataclass
from datetime import datetime
from typing import List

from infrastructure.api.adapter import to_asset_entity
from infrastructure.api.client import AlpacaApiClient
from infrastructure.db.client import PostgresClient
from infrastructure.db.model.asset import AssetTableMetaData
from infrastructure.db.model.common import TableDataset

from .entity import Asset
from .value import AssetType


@dataclass
class AssetRepository:
    psql_client: PostgresClient
    trading_client: AlpacaApiClient

    def fetch_assets(self, asset_type: AssetType) -> List[Asset]:
        if asset_type is AssetType.STOCK:
            data = self.trading_client.fetch_stock_assets()
        elif asset_type is AssetType.CRYPTO:
            data = self.trading_client.fetch_crypto_assets()
        else:
            raise ValueError(f"Invalid asset_type: {asset_type}")
        return to_asset_entity(data)

    def store_assets(self, assets: List[Asset]):
        # Same version at this time
        version: datetime = datetime.now()
        # Add version info to assets
        for asset in assets:
            asset.version = version
        # create table dataset for insert
        asset_table_dataset = TableDataset(
            metadata=AssetTableMetaData(),
            records=assets
        )
        # store assets
        self.psql_client.store_table_dataset(asset_table_dataset)