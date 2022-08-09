from fastapi import Depends
from sqlalchemy.orm import Session


from app.config.database import get_db


class BaseRouting:
    session: Session = Depends(get_db)
