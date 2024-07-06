from datetime import datetime
from src.database import OhlcModel
from .. import OhlcRepositoryInterface
from .base_repository import BaseSQLRepository

class OhlcSQLRepository(OhlcRepositoryInterface, BaseSQLRepository):
    def __init__(self):
        super().__init__(OhlcModel)

    def get_last_delta(self, symbol: str):
        return self.model.select().where(self.model.symbol == symbol).order_by(self.model.datetime.desc()).dicts().first()
    
    def is_updated(self, symbol: str):
        last_delta = self.get_last_delta(symbol=symbol)
        if last_delta is None:
            return False
        return last_delta["datetime"].date() == datetime.now().date()
    
    def is_new_delta(self, symbol: str, delta_datetime: str):
        last_delta = self.get_last_delta(symbol=symbol)
        if last_delta is None:
            return True
        return last_delta["datetime"].date() < datetime.strptime(delta_datetime, "%Y-%m-%d %H:%M:%S").date()