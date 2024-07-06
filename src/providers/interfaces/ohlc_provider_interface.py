from typing import Any, Hashable
from abc import ABC, abstractmethod

class OhlcProviderInterface(ABC):
    @abstractmethod
    def get_ohlc_full(self, fsym: str, tsym = str) -> list[dict[Hashable, Any]]:
        pass

    @abstractmethod
    def get_ohlc_limited(self, fsym: str, tsym: str, limit: int) -> list[dict[Hashable, Any]]:
        pass