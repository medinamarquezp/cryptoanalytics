from peewee import *
from .base_model import BaseModel

class PriceModel(BaseModel):
    timestamp = IntegerField()
    datetime = DateTimeField()
    year = IntegerField()
    high = FloatField()
    low = FloatField()
    open = FloatField()
    close = FloatField()
    symbol = CharField()
    candel_color = CharField()
    percent_change = FloatField()
    

    class Meta:
        db_table = 'prices'