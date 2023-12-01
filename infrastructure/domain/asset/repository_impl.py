# infrastructure/asset/repository.py
from datetime import datetime
from typing import List

from pydantic import BaseModel

from domain.asset.entity import Asset
from domain.asset.repository import AssetRepository
from domain.asset.value import AssetType
from infrastructure.client.api.alpaca import AlpacaApiClient
from infrastructure.client.db.data_model import TableDataset
from infrastructure.client.db.psql import PostgresClient
from infrastructure.domain.asset.data_model import AssetTableMetaData


class AssetRepositoryImpl(AssetRepository, BaseModel):
    psql_client: PostgresClient
    trading_client: AlpacaApiClient

    def fetch_assets(self, asset_type: AssetType) -> List[Asset]:
        if asset_type is AssetType.STOCK:
            data = self.trading_client.fetch_stock_assets()
        elif asset_type is AssetType.CRYPTO:
            data = self.trading_client.fetch_crypto_assets()
        else:
            raise ValueError(f"Invalid asset_type: {asset_type}")
        return [Asset(**asset_data) for asset_data in data]

    def stage_asset_storing(self, assets: List[Asset], version: datetime):
        # Add version info to assets
        for asset in assets:
            asset.version = version
        # create table dataset for insert
        asset_table_dataset = TableDataset(
            metadata=AssetTableMetaData(),
            records=assets
        )
        # Parallel insert for speed
        with self.psql_client.create_session() as session:
            self.psql_client.schedule_parallel_insert_models(asset_table_dataset, session)