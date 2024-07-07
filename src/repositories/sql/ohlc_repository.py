from datetime import datetime
from typing import Optional
from src.database import OhlcModel
from .. import OhlcRepositoryInterface
from .base_repository import BaseSQLRepository

class OhlcSQLRepository(OhlcRepositoryInterface, BaseSQLRepository):
    def __init__(self):
        super().__init__(OhlcModel)

    def is_empty(self, symbol: str):
        return self.count(filter={"symbol": symbol}) == 0

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
    
    def get_deltas_from(self, symbol: str, date_from: Optional[datetime] = None):
        query = self.model.select().where(self.model.symbol == symbol)
        if date_from is not None:
            query = query.where(self.model.datetime >= date_from)
        return list(query.dicts())
        