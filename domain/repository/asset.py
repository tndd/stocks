from datetime import datetime
from typing import List

from client import AlpacaApiClient, PostgresClient
from pydantic import BaseModel
from sqlalchemy.orm import Session

from common.decorators import count_time
from domain.model.asset import Asset


class AssetRepository(BaseModel):
    psql_client: PostgresClient
    trading_client: AlpacaApiClient

    @count_time
    def stage_assets(self, data: List[dict], version: datetime, session: Session):
        # Add version info to data
        data_with_version = [{'version': version, **asset} for asset in data]
        # Parallel insert for speed
        self.psql_client.schedule_parallel_insert_models(Asset, data_with_version, session)
