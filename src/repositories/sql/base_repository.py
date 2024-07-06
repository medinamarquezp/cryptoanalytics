from functools import reduce
from .. import BaseRepositoryInterface

class BaseSQLRepository(BaseRepositoryInterface):
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
    
    def insert(self, data: dict):
        return self.model.create(data)
    
    def insert_many(self, data: list[dict]):
        self.model.insert_many(data).execute()

    def update(self, id: str, data: dict):
        self.model.update(data).where(self.model.id == id).execute()
    
    def upsert_many(self, data: list[dict], conflict_target: list[str]):
        self.model.insert_many(data).on_conflict(
            conflict_target=[getattr(self.model, key) for key in conflict_target],
            update={key: getattr(self.model, key) for key in data[0].keys()}
        ).execute()

    def delete_where(self, filters: dict):
        return self.model.delete().where(
            self.__parse_filters(filters)
        ).execute()
    
    def delete_all(self):
        self.model.delete().execute()
    
    def __parse_filters(self, filters: dict):
        return reduce(lambda x, y: x & y, (getattr(self.model, key) == value for key, value in filters.items()))
