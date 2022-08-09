from typing import List

from sqlalchemy.orm import Session

from app.schemas.accounts.user import UserSchema
from app.models.accounts.user import User


def create_user(user: UserSchema, db: Session):
    db_user = User(
        username=user.username,
        email=user.email,
        birthday=user.birthday,
        password=user.password,
        created_by='ADMIN'
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db):
    return db.query(User).all()
