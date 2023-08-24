from peewee import *

db = SqliteDatabase('contacts.db')


class Contact(Model):
    first_name = CharField()
    last_name = CharField()
    phone = CharField()

    class Meta:
        database = db
