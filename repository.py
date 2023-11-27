from dataclasses import dataclass
from datetime import datetime
from typing import List

from sqlalchemy.orm import Session

from client import AlpacaApiClient, PostgresClient
from decorators import count_time
from model import Asset


@dataclass
class AssetRepository:
    psql_client: PostgresClient
    trading_client: AlpacaApiClient

    @count_time
    def stage_assets(self, data: List[dict], version: datetime, session: Session):
        data_with_version = [{'version': version, **asset} for asset in data]
        self.psql_client.schedule_parallel_insert_models(Asset, data_with_version, session)
