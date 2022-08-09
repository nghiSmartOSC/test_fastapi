from datetime import datetime
import factory

from app.models.accounts.user import User as UserModel
from tests.feature.base import session




class UserFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = UserModel
        sqlalchemy_session = session
        sqlalchemy_session_persistence = "flush"
    
    username = 'a'
    email = 'b'
    password = 'c'
    birthday = '2022-06-06'
    is_active = True
    created_date = datetime.utcnow()
    created_by = 'Admin'
