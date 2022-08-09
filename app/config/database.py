import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_db(database_url):
    engine = create_engine(database_url)
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return engine, session()


async def get_db():
    _, db = create_db(os.environ['DATABASE_URL'])
    try:
        yield db
    finally:
        db.close()
