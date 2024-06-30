from abc import ABC
from functools import reduce

class BaseRepository(ABC):
    def __init__(self, model):
        self.model = model

    def get_all(self, filter: dict = {}):
        if filter:
            return list(self.model.select().where(
                self.__parse_filters(filter)
            ).dicts())
        return list(self.model.select().dicts())

    def get_by_id(self, id: str):
        return self.model.select().where(self.model.id == id).dicts().first()
    
    def count(self, filter: dict = {}):
        return len(self.get_all(filter))
    
    def insert(self, ohlc_raw: dict):
        return self.model.insert(ohlc_raw).execute()
    
    def insert_many(self, ohlc_raw: list[dict]):
        self.model.insert_many(ohlc_raw).execute()

    def update(self, id: str, ohlc_raw: dict):
        self.model.update(ohlc_raw).where(self.model.id == id).execute()
    
    def upsert_many(self, ohlc_raw: list[dict], conflict_target: list[str]):
        self.model.insert_many(ohlc_raw).on_conflict(
            conflict_target=[getattr(self.model, key) for key in conflict_target],
            update={key: getattr(self.model, key) for key in ohlc_raw[0].keys()}
        ).execute()

    def delete_where(self, filters: dict):
        return self.model.delete().where(
            self.__parse_filters(filters)
        ).execute()
    
    def delete_all(self):
        self.model.delete().execute()
    
    def __parse_filters(self, filters: dict):
        return reduce(lambda x, y: x & y, (getattr(self.model, key) == value for key, value in filters.items()))
