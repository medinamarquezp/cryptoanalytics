from datetime import datetime
from ..database import Ohlc
from .base_repository import BaseRepository

class OhlcRepository(BaseRepository):
    def __init__(self):
        super().__init__(Ohlc)

    def get_last_delta(self, symbol: str):
        return self.model.select().where(self.model.symbol == symbol).order_by(self.model.datetime.desc()).dicts().first()
    
    def is_updated(self, symbol: str):
        last_delta = self.get_last_delta(symbol=symbol)
        return last_delta["datetime"].date() == datetime.now().date()
    
    def is_new_delta(self, symbol: str, delta_datetime: str):
        last_delta = self.get_last_delta(symbol=symbol)
        return last_delta["datetime"].date() < datetime.strptime(delta_datetime, "%Y-%m-%d %H:%M:%S").date()