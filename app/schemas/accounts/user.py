from datetime import date

from pydantic import (
    BaseModel,
    constr,
)

class UserSchema(BaseModel):

    username: constr(min_length=6)
    email: constr(min_length=8)
    password: constr(min_length=8, max_length=255)
    birthday: date

    class Config:
        orm_mode = True
