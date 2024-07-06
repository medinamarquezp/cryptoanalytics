from src.database import PriceModel
from .base_repository import BaseSQLRepository

class PriceSQLRepository(BaseSQLRepository):
    def __init__(self):
        super().__init__(PriceModel)