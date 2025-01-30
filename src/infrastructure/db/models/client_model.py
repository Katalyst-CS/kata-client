import datetime
import uuid

from peewee import Model, CharField, UUIDField, ForeignKeyField, DateTimeField

from src.infrastructure.db.database import db

#TODO Pendiente de terminar.

class Client(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4())
    customer_CharField =CharField (choices=[('PERSON', 'person'), 'ORGANIZATION', 'organization'])
    status = CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')])
    tax_id = CharField(max_length=30)
    indentifier = CharField(max_length=100)
    foreing_reference = ForeignKeyField()
    date_created = DateTimeField(default=datetime.now)
    date_modified = DateTimeField(default=datetime.now)

    class Meta():
        database = db
        table_name = "clients"
