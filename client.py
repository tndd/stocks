from contextlib import closing
from dataclasses import dataclass
from typing import List

from alpaca.trading.client import TradingClient
from alpaca.trading.enums import AssetClass
from alpaca.trading.requests import GetAssetsRequest
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import text

from models import Base


@dataclass
class PostgresClient:
    database: str = "stocks"
    user: str = "postgres"
    password: str = "postgres"
    host: str = "localhost"
    port: str = "5432"
    engine: Engine = None

    def __post_init__(self):
        self.engine = create_engine(
            f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'
        )

    def create_session(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return closing(session)

    def truncate_insert_models(self, model: Base, data: List[dict]):
        model.metadata.create_all(self.engine)
        with self.create_session() as session:
            session.query(model).delete()
            session.bulk_insert_mappings(model, data)
            session.commit()

    def insert_models(self, model: Base, data: List[dict]):
        model.metadata.create_all(self.engine)
        with self.engine.connect() as conn:
            conn.execute(text("""
                INSERT INTO assets VALUES (
                    :id,
                    :asset_class,
                    :exchange,
                    :symbol,
                    :name,
                    :status,
                    :tradable,
                    :marginable,
                    :shortable,
                    :easy_to_borrow,
                    :fractionable,
                    :maintenance_margin_requirement,
                    :attributes,
                    :min_order_size,
                    :min_trade_increment,
                    :price_increment
                ) ON CONFLICT (id) DO NOTHING
            """), data)
            conn.commit()


@dataclass
class AlpacaApiClient:
    api_key: str
    secret_key: str
    trading_client: TradingClient = None

    def __post_init__(self):
        self.trading_client = TradingClient(self.api_key, self.secret_key)

    def fetch_assets(self, asset_class: AssetClass) -> List[dict]:
        search_params = GetAssetsRequest(asset_class=asset_class)
        assets = self.trading_client.get_all_assets(search_params)
        return [asset.model_dump() for asset in assets]

    def fetch_assets_stock(self) -> List[dict]:
        return self.fetch_assets(asset_class=AssetClass.US_EQUITY)

    def fetch_assets_crypto(self) -> List[dict]:
        return self.fetch_assets(asset_class=AssetClass.CRYPTO)


if __name__ == '__main__':
    import os

    from dotenv import load_dotenv

    load_dotenv()

    api_key = os.getenv('API_KEY')
    secret_key = os.getenv('SECRET_KEY')
    alpaca_api_client = AlpacaApiClient(api_key, secret_key)