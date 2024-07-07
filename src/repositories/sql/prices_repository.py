from src.database import PriceModel
from .base_repository import BaseSQLRepository

class PricesSQLRepository(BaseSQLRepository):
    def __init__(self):
        super().__init__(PriceModel)