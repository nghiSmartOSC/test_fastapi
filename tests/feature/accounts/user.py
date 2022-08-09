from tests.feature.base import BaseTestCaseDB
from tests.factories.accounts.user import UserFactory


class TestUser(BaseTestCaseDB):
    def setUp(self):
        print("ajsjha")
        super().setUp()
        UserFactory.create()
    
    def test_get_user(self):
        response = self.client.get("/api/v1/user")
        data = response.json()
        self.assertEqual(response.status_code, 200)
        print(data)