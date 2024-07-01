from ..services import log
from ..repositories import OhlcRepository
from ..providers import CryptocompareProvider

def import_all(symbol: str):
    try:
        log.info(f"Deleting all {symbol} ohlc rows from database")
        total_deleted = OhlcRepository().delete_where(filters={"symbol": symbol})
        log.info(f"Deleted {total_deleted} {symbol} ohlc rows from database")
        ohlc_inputs = CryptocompareProvider().get_ohlc_full(fsym=symbol)
        log.info(f"Obtained {len(ohlc_inputs)} ohlc inputs from CryptocompareProvider API")
        OhlcRepository().insert_many(ohlc_inputs)
        log.info("Inserted all ohlc inputs into database")
        return True
    except Exception as e:
        log.error(f"Something went wrong on importing all ohlc inputs: {e}")
        return False 

def import_last_delta(symbol: str):
    try:
        is_updated = OhlcRepository().is_updated(symbol=symbol)
        if is_updated:
            log.info(f"{symbol} ohlc rows are updated")
            return False
        delta = CryptocompareProvider().get_ohlc_limit(fsym=symbol, limit=1)
        log.info(f"Obtained last {symbol} ohlc delta from Cryptocompare API for {delta['datetime']}")
        is_new_delta = OhlcRepository().is_new_delta(symbol=symbol, delta_datetime=delta['datetime'])
        if not is_new_delta:
            log.info(f"{symbol} ohlc delta is not new")
            return False
        inserted_ohlc = OhlcRepository().insert(delta)
        log.info(f"Inserted last {symbol} ohlc register into database with id {inserted_ohlc.id}")
        return True
    except Exception as e:
        log.error(f"Something went wrong on import last delta: {e}")
        return False
