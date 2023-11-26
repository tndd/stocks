from dataclasses import dataclass

from client import AlpacaApiClient, PostgresClient
from models import Asset


@dataclass
class AssetRepository:
    psql_client: PostgresClient
    trading_client: AlpacaApiClient

    def store_assets(self, data):
        self.psql_client.insert_models(Asset, data)

    def fetch_store_assets_stock(self):
        fetched_data = self.trading_client.fetch_assets_stock()
        self.store_assets(fetched_data)

    def fetch_store_assets_crypto(self):
        fetched_data = self.trading_client.fetch_assets_crypto()
        self.store_assets(fetched_data)

    def fetch_store_assets_all(self):
        self.fetch_store_assets_stock()
        self.fetch_store_assets_crypto()


if __name__ == '__main__':
    import os

    from dotenv import load_dotenv

    load_dotenv()

    api_key = os.getenv('API_KEY')
    secret_key = os.getenv('SECRET_KEY')

    psql_client = PostgresClient()
    alpaca_api_client = AlpacaApiClient(api_key, secret_key)

    asset_rp = AssetRepository(psql_client, alpaca_api_client)
    asset_rp.fetch_store_assets_all()