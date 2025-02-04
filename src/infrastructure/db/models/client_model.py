from datetime import datetime
import uuid

from peewee import Model, CharField, UUIDField, DateTimeField

from infrastructure.db.db_connection.database import db


class Client(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    customer_type = CharField(choices=[('PERSON', 'person'), ('ORGANIZATION', 'organization')])
    status = CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], default='ACTIVE')
    tax_id = CharField(max_length=30, null=True)
    identifier = CharField(max_length=100, unique=True)
    foreign_reference = UUIDField(null=True)
    date_created = DateTimeField(default=datetime.now)
    date_modified = DateTimeField(default=datetime.now)

    class Meta():
        database = db
        table_name = "clients"
