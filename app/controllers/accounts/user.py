from typing import List

from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from app.controllers.base.base_url import BaseRouting
from app.schemas.accounts.user import UserSchema
from app.services.accounts.user import (
    create_user,
    get_users
)


router = InferringRouter()


@cbv(router=router)
class User(BaseRouting):

    @router.post("/")
    def create_user(self, user: UserSchema):
        user_response = create_user(user, self.session)
        return user_response

    @router.get("/")
    def get_user(self):
        return get_users(self.session)
