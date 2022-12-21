from crub.users.user_db import register_user
from models.users.models import UserModel
from core.database import get_db
from datetime import datetime

db = get_db()


def create_tables():
    db.create_tables([UserModel])

def interface():
    name = input('Введите имя: ')
    age = input('Введите возраст: ')
    birth_date = input('Введите дату рождения: ')
    register_user(name=name, age=age, birth_date=datetime.now())

if __name__ == '__main__':
    create_tables()
    interface()