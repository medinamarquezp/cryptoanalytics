from .instance import db
from .models.ohlc import Ohlc

db.connect()
db.create_tables([Ohlc], safe=True)
