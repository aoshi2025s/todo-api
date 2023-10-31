from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

#下記URLに定義したMYSQLのDockerコンテナに対して接続するセッションを作成
#get_db()関数を通してこのセッションを取得し、DBへあくせすする

DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"

db_engine = create_engine(DB_URL,echo=True)
db_session = sessionmaker(autocommit=False,autoflush=False,bind=db_engine)

Base = declarative_base()

def get_db():
    with db_sessoin() as session:
        yield session

