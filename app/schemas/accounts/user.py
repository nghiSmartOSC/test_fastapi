from datetime import date

from pydantic import constr
from fastapi_utils.api_model import APIModel

class UserSchema(APIModel):

    username: constr(min_length=6)
    email: constr(min_length=8)
    password: constr(min_length=8, max_length=255)
    birthday: date

    class Config:
        orm_mode = True
