from peewee import *

db = PostgresqlDatabase('Contact', user='rebekah',
                        password='', host='localhost', port=5432)


class BaseModel(Model):
    class Meta:
        database = db


class Contact(BaseModel):
    first_name = CharField()
    last_name = CharField()
    phone = IntegerField()
