from ..database import PriceModel
from .base_repository import BaseRepository

class OhlcRepository(BaseRepository):
    def __init__(self):
        super().__init__(PriceModel)