# infrastructure/asset/repository.py
from datetime import datetime
from typing import List

from sqlalchemy.orm import Session

from common.decorators import count_time
from domain.asset.repository import AssetRepository
from infrastructure.common.api.alpaca import AlpacaApiClient
from infrastructure.common.db.psql import PostgresClient


class AssetRepositoryImpl(AssetRepository):
    psql_client: PostgresClient
    trading_client: AlpacaApiClient

    def __init__(self, psql_client: PostgresClient, trading_client: AlpacaApiClient):
        self.psql_client = psql_client
        self.trading_client = trading_client

    def stage_assets(self, data: List[dict], version: datetime):
        # Add version info to data
        data_with_version = [{'version': version, **asset} for asset in data]
        # Parallel insert for speed
        with self.psql_client.create_session() as session:
            self.psql_client.schedule_parallel_insert_models(Asset, data_with_version, session)