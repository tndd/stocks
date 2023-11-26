import os

from alpaca.trading.client import TradingClient
from alpaca.trading.enums import AssetClass
from alpaca.trading.requests import GetAssetsRequest
from dotenv import load_dotenv

from models import Asset
from postgres import insert_models_to_db

load_dotenv()
api_key = os.getenv('API_KEY')
secret_key = os.getenv('SECRET_KEY')

trading_client = TradingClient(api_key, secret_key)
search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)
assets_data = trading_client.get_all_assets(search_params)

# Call the function to insert the data into the database
insert_models_to_db(Asset, assets_data)
