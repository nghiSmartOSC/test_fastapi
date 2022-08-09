import os
from abc import ABC
from fastapi import FastAPI


from app.controllers import routers


class ISetting(ABC):
    PROJECT_NAME: str
    PROJECT_VERSION: str

    def get_config(self):
        return {'title': self.PROJECT_NAME, 'version': self.PROJECT_VERSION}


class ISettingDB(ISetting):
    DB_URL: str


class DevSettings(ISettingDB):
    PROJECT_NAME: str = "Dev API"
    PROJECT_VERSION: str = "1.0.0"
    DB_URL: str = os.environ['DATABASE_URL']


class TestSettings(ISettingDB):
    PROJECT_NAME: str = "Test API"
    PROJECT_VERSION: str = "1.0.0"
    DB_URL: str = os.environ['DATABASE_URL_TEST']


def set_router(app: FastAPI, routers):
    for route in routers:
        app.include_router(route.route, prefix=route.prefix)


def start_application(settings: ISetting):
    config = settings.get_config()
    app = FastAPI(**config)
    set_router(app, routers)
    return app
