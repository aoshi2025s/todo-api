from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import sessionmaker,declarative_base

#下記URLに定義したMYSQLのDockerコンテナに対して接続するセッションを作成
#get_db()関数を通してこのセッションを取得し、DBへあくせすする

ASYNC_DB_URL = "mysql+aiomysql://root@db:3306/demo?charset=utf8"

async_engine = create_async_engine(ASYNC_DB_URL,echo=True)
async_session = sessionmaker(autocommit=False,autoflush=False,bind=async_engine,class_=AsyncSession)

Base = declarative_base()

async def get_db():
    async with async_session() as session:
        yield session

