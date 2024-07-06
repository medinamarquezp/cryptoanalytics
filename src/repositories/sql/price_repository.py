from database import PriceModel
from .. import BaseRepositoryInterface
from .base_repository import BaseSQLRepository

class PriceSQLRepository(BaseRepositoryInterface, BaseSQLRepository):
    def __init__(self):
        super().__init__(PriceModel)