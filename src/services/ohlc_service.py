from ..shared import log, days_till_today
from ..providers import OhlcProviderInterface
from ..repositories import OhlcRepositoryInterface

class OhlcService:
    __default_symbol = "BTC"

    def __init__(
            self, 
            repository: OhlcRepositoryInterface, 
            provider: OhlcProviderInterface,
            symbol: str = __default_symbol
        ):
        self.repository = repository
        self.provider = provider
        self.symbol = symbol

    def set_symbol(self, symbol: str):
        self.symbol = symbol

    def get_all(self):
        return self.repository.get_all(filter={"symbol": self.symbol})
    
    def get_last_delta(self):
        return self.repository.get_last_delta(symbol=self.symbol)

    def is_empty(self):
        return self.repository.is_empty(symbol=self.symbol)

    def is_updated(self):
        return self.repository.is_updated(symbol=self.symbol)

    def import_all(self):
        try:
            log.info(f"Deleting all {self.symbol} ohlc rows from database")
            total_deleted = self.repository.delete_where(filters={"symbol": self.symbol})
            log.info(f"Deleted {total_deleted} {self.symbol} ohlc rows from database")
            ohlc_inputs = self.provider.get_ohlc_full(fsym=self.symbol)
            log.info(f"Obtained {len(ohlc_inputs)} ohlc inputs from CryptocompareProvider API")
            self.repository.insert_many(ohlc_inputs)
            log.info("Inserted all ohlc inputs into database")
            return True
        except Exception as e:
            log.error(f"Something went wrong on importing all ohlc inputs: {e}")
            return False
        
    def import_pending_deltas(self):
        try:
            is_updated = self.repository.is_updated(symbol=self.symbol)
            if is_updated:
                log.info(f"{self.symbol} ohlc rows are updated")
                return False
            last_delta = self.repository.get_last_delta(symbol=self.symbol)
            last_datetime = last_delta["datetime"]
            log.info(f"Last {self.symbol} ohlc delta datetime is {last_datetime}")
            pending_deltas = days_till_today(last_datetime)
            log.info(f"Obtained {pending_deltas} pending deltas from last {self.symbol} ohlc delta")
            ohlc_deltas = self.provider.get_ohlc_limited(fsym=self.symbol, limit=pending_deltas)
            log.info(f"Obtained {len(ohlc_deltas)} ohlc deltas from Cryptocompare API")
            self.repository.upsert_many(ohlc_deltas, conflict_target=["symbol", "timestamp"])
            log.info(f"All pending {self.symbol} ohlc deltas were inserted into database")
            return True
        except Exception as e:
            log.error(f"Something went wrong on import pending deltas: {e}")
            return False