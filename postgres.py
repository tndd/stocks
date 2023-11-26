import json
import time

import pandas as pd
from sqlalchemy import Boolean, Column, Float, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# PostgreSQL database details
database = "stock_data"
user = "postgres"
password = "postgres"
host = "localhost"
port = "5432"

# Create engine
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

# Create a Session
Session = sessionmaker(bind=engine)
session = Session()

# Define the Asset class
Base = declarative_base()

class Asset(Base):
    __tablename__ = 'assets'

    id = Column(String, primary_key=True)
    asset_class = Column(String)
    exchange = Column(String)
    symbol = Column(String)
    name = Column(String)
    status = Column(String)
    tradable = Column(Boolean)
    marginable = Column(Boolean)
    shortable = Column(Boolean)
    easy_to_borrow = Column(Boolean)
    fractionable = Column(Boolean)
    min_order_size = Column(Float)
    min_trade_increment = Column(Float)
    price_increment = Column(Float)
    maintenance_margin_requirement = Column(Float)
    attributes = Column(String)

# assets.jsonからデータを読み込む
with open('assets.json') as f:
    data = json.load(f)

# データをPandas DataFrameに変換
df = pd.DataFrame(data)

# テーブルを作成
Base.metadata.create_all(engine)

# データを削除
session.query(Asset).delete()
session.commit()

# データを挿入
start_time = time.time()
df.to_sql(Asset.__tablename__, engine, if_exists='append', index=False, method='multi')
end_time = time.time()

print(f"この一連の処理にかかった時間: {end_time - start_time} 秒")

