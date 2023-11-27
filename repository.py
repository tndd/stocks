from dataclasses import dataclass
from datetime import datetime
from typing import List

from sqlalchemy.orm import Session

from client import AlpacaApiClient, PostgresClient
from decorators import count_time
from models import Asset


@dataclass
class AssetRepository:
    psql_client: PostgresClient
    trading_client: AlpacaApiClient

    @count_time
    def stage_assets(self, data: List[dict], version: datetime, session: Session):
        data_with_version = [{'version': version, **asset} for asset in data]
        self.psql_client.insert_models(Asset, data_with_version)


@dataclass
class AssetService:
    asset_repositoy: AssetRepository

    def fetch_stage_assets_stock(self, version: datetime, session: Session):
        fetched_data = self.trading_client.fetch_assets_stock()
        self.asset_repositoy.stage_assets(fetched_data, version, session)

    def fetch_stage_assets_crypto(self, version: datetime, session: Session):
        fetched_data = self.trading_client.fetch_assets_crypto()
        self.asset_repositoy.stage_assets(fetched_data, version, session)

    def update_assets(self):
        version: datetime = datetime.now()
        session: Session = self.psql_client.create_session()
        try:
            session.begin()
            self.fetch_stage_assets_stock(version, session)
            self.fetch_stage_assets_crypto(version, session)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
