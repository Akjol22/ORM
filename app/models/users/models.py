import peewee as pw
from core.database import get_db


class UserModel(pw.Model):
    name = pw.CharField(max_length=100)
    age = pw.SmallIntegerField()
    birth_date = pw.DateField()


    class Meta:
        database = get_db()