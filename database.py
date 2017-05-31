from peewee import PostgresqlDatabase, Model, CharField

DATABASE = 'webapp'
db = PostgresqlDatabase(DATABASE, threadlocals=True)


class BaseModel(Model):
    class Meta:
        database = db


class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    miscellaneous = CharField()
