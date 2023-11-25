import json
import os
import time

from alpaca.trading.client import TradingClient
from alpaca.trading.enums import AssetClass
from alpaca.trading.requests import GetAssetsRequest
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')
secret_key = os.getenv('SECRET_KEY')


trading_client = TradingClient(api_key, secret_key)


search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)
assets = trading_client.get_all_assets(search_params)

start_time = time.time()
assets_json = [json.loads(asset.model_dump_json()) for asset in assets]
with open('assets.json', 'w', encoding='utf-8') as f:
    json.dump(assets_json, f, ensure_ascii=False, indent=4)
end_time = time.time()
print(f"この一連の処理にかかった時間: {end_time - start_time} 秒")

