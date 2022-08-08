from app.models.core import BaseModelMeta
from sqlalchemy import Column, String, Date, Boolean


class User(BaseModelMeta):

    __tablename__ = 'user'

    username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255, nullable=False), unique=True)
    password = Column(String(255), nullable=False)
    birthday = Column(Date, nullable=False)
    is_active = Column(Boolean, default=False)

