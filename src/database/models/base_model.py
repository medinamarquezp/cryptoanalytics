import uuid
import datetime
from peewee import *
from ..instance import db

class BaseModel(Model):
    id = UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
        abstract = True

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.now()
        return super(BaseModel, self).save(*args, **kwargs)
