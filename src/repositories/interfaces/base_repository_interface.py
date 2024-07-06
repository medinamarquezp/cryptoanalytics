from abc import ABC, abstractmethod

class BaseRepositoryInterface(ABC):
    @abstractmethod
    def get_all(self, filter: dict = {}) -> list[dict]:
        pass

    @abstractmethod
    def get_by_id(self, id: str) -> dict:
        pass
    
    @abstractmethod
    def count(self, filter: dict = {}) -> int:
        pass
    
    @abstractmethod
    def insert(self, data: dict):
        pass
    
    @abstractmethod
    def insert_many(self, data: list[dict]):
        pass

    @abstractmethod
    def update(self, id: str, data: dict):
        pass
    
    @abstractmethod
    def upsert_many(self, data: list[dict], conflict_target: list[str]):
        pass

    @abstractmethod
    def delete_where(self, filters: dict):
        pass
    
    @abstractmethod
    def delete_all(self):
        pass