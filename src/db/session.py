from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from .base import ModelBase
from contents.models import Quote, Article

DATABASE_URL = "sqlite:///./quotes.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


if not database_exists(engine.url):
    create_database(engine.url)

ModelBase.metadata.create_all(bind=engine)


@contextmanager
def get_db():
    """
    호출되면 DB 연결하고 작업 완료되면 close
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
