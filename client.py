from concurrent.futures import ProcessPoolExecutor
from contextlib import closing
from dataclasses import dataclass
from typing import List

from alpaca.trading.client import TradingClient
from alpaca.trading.enums import AssetClass
from alpaca.trading.requests import GetAssetsRequest
from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session, sessionmaker

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

    def schedule_insert_models(self, model: Base, models: List[dict], session: Session):
        # Ignore duplicate keys.
        table = model.__table__
        stmt = insert(table).values(models)
        do_nothing_stmt = stmt.on_conflict_do_nothing(index_elements=['id'])
        session.execute(do_nothing_stmt)

    def schedule_parallel_insert_models(self, model: Base, data: List[dict], session: Session, n_worker: int = 8):
        model.metadata.create_all(self.engine)
        n_chunk = len(data) // n_worker
        batches = [data[i:i + n_chunk] for i in range(0, len(data), n_chunk)]
        with ProcessPoolExecutor(max_workers=n_worker) as executor:
            for batch in batches:
                executor.submit(self.schedule_insert_models, model, batch, session)


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