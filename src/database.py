from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from constants import SQLALCHEMY_DB_URL

engine = create_engine(SQLALCHEMY_DB_URL)

if not database_exists(engine.url):
    create_database(engine.url)

print(f"{database_exists(engine.url)=}")


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
        
