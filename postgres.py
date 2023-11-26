import time
from contextlib import closing

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

# PostgreSQL database details
database = "stocks"
user = "postgres"
password = "postgres"
host = "localhost"
port = "5432"

# Create engine
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

def create_db_session():
    Session = sessionmaker(bind=engine)
    session = Session()
    return closing(session)


def insert_models_to_db(model: Base, data):
    # テーブルを作成
    model.metadata.create_all(engine)
    # データの削除と挿入
    with create_db_session() as session:
        # 削除
        session.query(model).delete()
        # 挿入
        start_time = time.time()
        session.bulk_insert_mappings(model, data)
        session.commit()
        end_time = time.time()
        print(f"insert_models_to_db: {end_time - start_time} sec")
