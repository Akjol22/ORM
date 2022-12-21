import peewee as pw
from core.settings import settings


def get_db():
    return pw.PostgresqlDatabase(settings.db)