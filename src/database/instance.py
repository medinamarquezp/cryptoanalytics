from peewee import SqliteDatabase
from ..config import SQLITE_DATABASE_PATH

db = SqliteDatabase(SQLITE_DATABASE_PATH)