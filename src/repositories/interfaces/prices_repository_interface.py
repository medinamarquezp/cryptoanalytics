from abc import abstractmethod
from .. import BaseRepositoryInterface

class PricesRepositoryInterface(BaseRepositoryInterface):
    @abstractmethod
    def get_last_price(self, symbol: str) -> dict:
        pass
    
    @abstractmethod
    def is_updated(self, symbol: str) -> bool:
        pass