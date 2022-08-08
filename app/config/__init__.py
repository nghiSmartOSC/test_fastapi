from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi_utils.inferring_router import InferringRouter

from app.config.base import ISetting
from app.controllers import router


def include_router(app: FastAPI, router: InferringRouter):
    app.include_router(router)


def start_application(settings: ISetting):
    config = settings.get_config()
    app = FastAPI(**config)
    include_router(app, router)
    return app


def create_db(database_url):
    engine = create_engine(database_url)
    session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return session


def get_db():
    pass
