from .instance import db
from .models.ohlc_model import OhlcModel
from .models.price_model import PriceModel

db.connect()
db.create_tables([OhlcModel, PriceModel], safe=True)
