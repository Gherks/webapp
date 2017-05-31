import os
from peewee import PostgresqlDatabase, Model, CharField
from playhouse.db_curl import connect

DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL:
    db = connect(DATABASE_URL)
else:
    DATABASE = 'webapp'
    db = PostgresqlDatabase(DATABASE)


class BaseModel(Model):
    class Meta:
        database = db


class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    miscellaneous = CharField()
