from abc import abstractmethod
from .. import BaseRepositoryInterface

class OhlcRepositoryInterface(BaseRepositoryInterface):
    @abstractmethod
    def is_empty(self, symbol: str) -> bool:
        pass

    @abstractmethod
    def get_last_delta(self, symbol: str) -> dict:
        pass
    
    @abstractmethod
    def is_updated(self, symbol: str) -> bool:
        pass
    
    @abstractmethod
    def is_new_delta(self, symbol: str, delta_datetime: str) -> bool:
        pass