from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

dbtype = "mysql+pymysql"
host = "localhost"
port = 8879
username = "root"
password = "root"
database = "Recipes"

SQLALCHEMY_DATABASE_URI = f"{dbtype}://{username}:{password}@{host}:{port}/{database}"

try:
    engine = create_engine(SQLALCHEMY_DATABASE_URI)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()
    print("MySQL Connection Established.")
except Exception as err:
    print("MySQL Connection Failed.")
    print(err)