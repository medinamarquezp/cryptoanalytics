from .instance import db
from .models.ohlc_model import OhlcModel

db.connect()
db.create_tables([OhlcModel], safe=True)
