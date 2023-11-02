from sqlalchemy import create_engine,text
from sqlalchemy.exc import InternalError,OperationalError

from api.models.task import Base
from api.database import DB_USER,DB_PASSWORD,DB_HOST,DB_PORT

#api/database.pyからDB接続用の定数を取得
DB_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/?charset=utf8"

DEMO_DB_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/demo?charset=utf8"
)

#ローカル用
#DB_URL = "mysql+pymysql://root@db:3306/demo?charset=utf8"
#engine = create_engine(DB_URL,echo=True)

engine = create_engine(DEMO_DB_URL,echo=True)

def database_exists():
    #接続を試みることでdemoデータベースの存在を確認
    try:
        engine.connect()
        return True
    except(OperationalError,InternalError) as e:
        print(e)
        print("database does not exist")
        return False

def create_database():
    if not database_exists():
        #demoデータベースがなければ作成する
        root = create_engine(DB_URL,echo=True)
        with root.connect() as conn:
            conn.execute(text("CREATE DATABASE demo"))
        print("created database")
    
    #DBモデルを元にテーブルを作成
    Base.metadata.create_all(bind=engine)
    print("created tables")

if __name__ == "__main__":
    create_database()


"""
def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()
"""
