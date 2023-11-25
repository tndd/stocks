import json
import time
import psycopg2

# PostgreSQL database details
database = "stock_data"
user = "postgres"
password = "postgres"
host = "localhost"
port = "5432"

# Create connection
conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
cur = conn.cursor()

# assets.jsonからデータを読み込む
with open('assets.json') as f:
    data = json.load(f)

# テーブルを作成
cur.execute("""
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
""")

# データを削除
cur.execute("""
    DELETE FROM assets
""")

# データを挿入
start_time = time.time()
for asset in data:
    cur.execute("""
        INSERT INTO assets VALUES (
            %(id)s,
            %(asset_class)s,
            %(exchange)s,
            %(symbol)s,
            %(name)s,
            %(status)s,
            %(tradable)s,
            %(marginable)s,
            %(shortable)s,
            %(easy_to_borrow)s,
            %(fractionable)s,
            %(min_order_size)s,
            %(min_trade_increment)s,
            %(price_increment)s
        )
    """, asset)
conn.commit()
end_time = time.time()
print(f"この一連の処理にかかった時間: {end_time - start_time} 秒")

