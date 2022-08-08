from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel(Base):

    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)


class BaseModelMeta(BaseModel):

    __abstract__ = True

    created_date = Column(DateTime, default=datetime.utcnow())
    created_by = Column(String(255), nullable=False)
    edited_date = Column(DateTime, onupdate=True)
    edited_by = Column(String(255), nullable=True)
    deleted_date = Column(DateTime, nullable=True)
    deleted_by = Column(String(255), nullable=True)