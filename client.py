import os
from contextlib import closing
from dataclasses import dataclass

from alpaca.trading.client import TradingClient
from alpaca.trading.enums import AssetClass
from alpaca.trading.requests import GetAssetsRequest
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker

from models import Base


@dataclass
class PostgresClient:
    database: str = "stocks"
    user: str = "postgres"
    password: str = "postgres"
    host: str = "localhost"
    port: str = "5432"
    engine: Engine

    def __post_init__(self):
        self.engine = create_engine(
            f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'
        )

    def create_session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return closing(session)

    def insert_models(self, model: Base, data):
        # WARN: This is not allow duplicate key.
        model.metadata.create_all(self.engine)
        with self.create_session() as session:
            session.query(model).delete()
            session.bulk_insert_mappings(model, data)
            session.commit()


@dataclass
class AlpacaApiClient:
    api_key: str
    secret_key: str
    trading_client: TradingClient

    def __post_init__(self):
        self.trading_client = TradingClient(self.api_key, self.secret_key)

    def get_assets(self, asset_class: AssetClass):
        search_params = GetAssetsRequest(asset_class)
        assets = self.trading_client.get_all_assets(search_params)
        return assets

    def get_assets_stock(self):
        return self.get_assets(asset_class=AssetClass.US_EQUITY)

    def get_assets_crypto(self):
        return self.get_assets(asset_class=AssetClass.CRYPTO)


if __name__ == '__main__':
    from dotenv import load_dotenv

    load_dotenv()

    api_key = os.getenv('API_KEY')
    secret_key = os.getenv('SECRET_KEY')
    alpaca_api_client = AlpacaApiClient(api_key, secret_key)