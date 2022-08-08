from typing import List

from app.controllers import router, cbv
from app.schemas.accounts.user import UserSchema
from app.models.accounts.user import User
from app.services.accounts.user import (
    create_user,
    get_users
)


@cbv(router=router)
class User:
    @router.post("/api/v1/user")
    def create_user(self, user: UserSchema) -> User:
        return create_user(user)

    @router.get("/api/v1/user")
    def get_user(self) -> List[User]:
        return get_users()