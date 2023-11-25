import json
import time

from sqlalchemy import create_engine
from sqlalchemy.sql import text

# PostgreSQL database details
database = "stock_data"
user = "postgres"
password = "postgres"
host = "localhost"
port = "5432"

# Create engine
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

# assets.jsonからデータを読み込む
with open('assets.json') as f:
    data = json.load(f)

# テーブルを作成
with engine.connect() as connection:
    connection.execute(text("""
        CREATE TABLE IF NOT EXISTS assets (
            id TEXT PRIMARY KEY,
            asset_class TEXT,
            exchange TEXT,
            symbol TEXT,
            name TEXT,
            status TEXT,
            tradable BOOLEAN,
            marginable BOOLEAN,
            shortable BOOLEAN,
            easy_to_borrow BOOLEAN,
            fractionable BOOLEAN,
            min_order_size REAL,
            min_trade_increment REAL,
            price_increment REAL
        )
    """))

    # データを削除
    connection.execute(text("""
        DELETE FROM assets
    """))

    # データを挿入
    start_time = time.time()
    connection.execute(text("""
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
            :min_order_size,
            :min_trade_increment,
            :price_increment
        )
    """), data)
    end_time = time.time()
    print(f"この一連の処理にかかった時間: {end_time - start_time} 秒")

