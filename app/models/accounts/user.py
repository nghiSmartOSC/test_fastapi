from app.models.core.base import BaseModelMeta
from sqlalchemy import Column, String, Date, Boolean, UniqueConstraint


class User(BaseModelMeta):

    __tablename__ = 'user'

    username = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
    birthday = Column(Date)
    is_active = Column(Boolean, default=False)

    __table_args__ = (
        UniqueConstraint('username', name='user_username_unique'),
        UniqueConstraint('email', name='user_email_unique'),
    )