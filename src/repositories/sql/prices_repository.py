from src.shared import datetime
from src.database import PriceModel
from .. import PricesRepositoryInterface
from .base_repository import BaseSQLRepository

class PricesSQLRepository(PricesRepositoryInterface, BaseSQLRepository):
    def __init__(self):
        super().__init__(PriceModel)

    def get_last_price(self, symbol: str):
        return self.model.select().where(self.model.symbol == symbol).order_by(self.model.datetime.desc()).dicts().first()

    def is_updated(self, symbol: str):
        last_price = self.get_last_price(symbol=symbol)
        if last_price is None:
            return False
        return last_price["datetime"].date() == datetime.now().date()