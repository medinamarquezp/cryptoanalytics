from os import getenv
from dotenv import load_dotenv

load_dotenv()

SQLITE_DATABASE_PATH = getenv("SQLITE_DATABASE_PATH")

CRYPTOCOMPARE = {
    "URL": getenv("CRYPTOCOMPARE_URL"),
    "KEY": getenv("CRYPTOCOMPARE_KEY")
}