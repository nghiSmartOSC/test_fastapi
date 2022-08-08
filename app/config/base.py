from abc import ABC
import os

BASE_DIR = os.path.abspath(os.curdir())

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
    DB_URL: str = os.environ['DB_URL_DEV']



class TestSettings(ISettingDB):
    PROJECT_NAME: str = "Test API"
    PROJECT_VERSION: str = "1.0.0"
    DB_URL: str = os.environ['DB_URL_TEST']


dev_settings = DevSettings()
test_setting = TestSettings()
