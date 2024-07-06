from ..shared import log
from ..repositories import OhlcSQLRepository
from ..providers import CryptocompareProvider
from ..utils.date_utils import days_till_today

def import_all(symbol: str):
    try:
        log.info(f"Deleting all {symbol} ohlc rows from database")
        total_deleted = OhlcSQLRepository().delete_where(filters={"symbol": symbol})
        log.info(f"Deleted {total_deleted} {symbol} ohlc rows from database")
        ohlc_inputs = CryptocompareProvider().get_ohlc_full(fsym=symbol)
        log.info(f"Obtained {len(ohlc_inputs)} ohlc inputs from CryptocompareProvider API")
        OhlcSQLRepository().insert_many(ohlc_inputs)
        log.info("Inserted all ohlc inputs into database")
        return True
    except Exception as e:
        log.error(f"Something went wrong on importing all ohlc inputs: {e}")
        return False
    
def import_pending_deltas(symbol: str):
    try:
        is_updated = OhlcSQLRepository().is_updated(symbol=symbol)
        if is_updated:
            log.info(f"{symbol} ohlc rows are updated")
            return False
        last_delta = OhlcSQLRepository().get_last_delta(symbol=symbol)
        last_datetime = last_delta["datetime"]
        log.info(f"Last {symbol} ohlc delta datetime is {last_datetime}")
        pending_deltas = days_till_today(last_datetime)
        log.info(f"Obtained {pending_deltas} pending deltas from last {symbol} ohlc delta")
        ohlc_deltas = CryptocompareProvider().get_ohlc_limited(fsym=symbol, limit=pending_deltas)
        log.info(f"Obtained {len(ohlc_deltas)} ohlc deltas from Cryptocompare API")
        OhlcSQLRepository().upsert_many(ohlc_deltas, conflict_target=["symbol", "timestamp"])
        log.info(f"All pending {symbol} ohlc deltas were inserted into database")
        return True
    except Exception as e:
        log.error(f"Something went wrong on import pending deltas: {e}")
        return False
