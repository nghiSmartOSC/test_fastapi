import os

from fastapi.testclient import TestClient
from unittest import TestCase
from dotenv import load_dotenv
from main import BASE_DIR
load_dotenv(os.path.join(BASE_DIR, '.env'))

from app.config.base import TestSettings, start_application
from app.config.database import create_db
from app.models.core.base import Base


engine, session = create_db(os.environ['DATABASE_URL_TEST'])


class BaseTestCase(TestCase):
    def setUp(self) -> None:
        super().setUp()
        app = start_application(TestSettings())
        self.client = TestClient(app)
    
    def tearDown(self) -> None:
        super().tearDown()


class BaseTestCaseDB(BaseTestCase):
    def setUp(self) -> None:
        super().setUp()
        Base.metadata.create_all(bind=engine)
    
    def tearDown(self) -> None:
        Base.metadata.drop_all(bind=engine)
        super().tearDown()
