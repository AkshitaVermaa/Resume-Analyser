from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
DATABASE_URL = "mysql+pymysql://2UxfjkRq6GoxkSZ.root:n5IlzGcaBOCG6Zzi@gateway01.ap-southeast-1.prod.alicloud.tidbcloud.com:4000/test"


engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
    connect_args={
        "ssl": {}
    }
)
SessionLocal=sessionmaker(bind=engine)
Base=declarative_base()