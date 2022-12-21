from models.users.models import UserModel
from shemas.user_schema import User
from datetime import datetime


def register_user(name: str, age: int, birth_date: datetime) -> UserModel:
    user = User(name=name, age=age, birth_date=birth_date)
    return UserModel.insert(user.dict()).execute()
