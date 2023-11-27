from dataclasses import dataclass
from datetime import datetime
from typing import List

from client import AlpacaApiClient, PostgresClient
from decorators import count_time
from models import Asset


@dataclass
class AssetRepository:
    psql_client: PostgresClient
    trading_client: AlpacaApiClient

    @count_time
    def store_assets(self, data: List[dict], version: datetime):
        data_with_version = [{'version': version, **asset} for asset in data]
        self.psql_client.insert_models(Asset, data_with_version)

    def fetch_store_assets_stock(self, version: datetime):
        fetched_data = self.trading_client.fetch_assets_stock()
        self.store_assets(fetched_data, version)

    def fetch_store_assets_crypto(self, version: datetime):
        fetched_data = self.trading_client.fetch_assets_crypto()
        self.store_assets(fetched_data, version)

    def update_assets(self):
        version: datetime = datetime.now()
        self.fetch_store_assets_stock(version)
        self.fetch_store_assets_crypto(version)


if __name__ == '__main__':
    import os

    from dotenv import load_dotenv

    load_dotenv()

    api_key = os.getenv('API_KEY')
    secret_key = os.getenv('SECRET_KEY')

    psql_client = PostgresClient()
    alpaca_api_client = AlpacaApiClient(api_key, secret_key)

    asset_rp = AssetRepository(psql_client, alpaca_api_client)
    asset_rp.update_assets()