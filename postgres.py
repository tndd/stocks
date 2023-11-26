import json
import time

from sqlalchemy import Boolean, Column, Float, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# PostgreSQL database details
database = "stocks"
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

# assets.jsonからデータを読み込む
with open('assets.json') as f:
    data = json.load(f)

# テーブルを作成
Base.metadata.create_all(engine)

# データを削除
session.query(Asset).delete()

# データを挿入
start_time = time.time()
session.bulk_insert_mappings(Asset, data)
session.commit()
end_time = time.time()
print(f"この一連の処理にかかった時間: {end_time - start_time} 秒")
