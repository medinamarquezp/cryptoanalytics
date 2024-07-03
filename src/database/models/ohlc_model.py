from peewee import *
from .base_model import BaseModel

class OhlcModel(BaseModel):
    timestamp = IntegerField()
    datetime = DateTimeField()
    high = FloatField()
    low = FloatField()
    open = FloatField()
    volumefrom = FloatField()
    volumeto = FloatField()
    close = FloatField()
    symbol = CharField()
    provider = CharField()

    class Meta:
        db_table = 'ohlc'
        indexes = (
            (('symbol', 'timestamp'), True),
        )