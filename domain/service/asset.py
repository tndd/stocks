from dataclasses import dataclass
from datetime import datetime

from sqlalchemy.orm import Session

from domain.repository.asset import AssetRepository


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
