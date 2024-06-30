import requests
import pandas as pd
from ..config import CRYPTOCOMPARE

class Cryptocompare():
    def __init__(self):
        self.url = CRYPTOCOMPARE["URL"]
        self.key = CRYPTOCOMPARE["KEY"]
        self.columns = ["time", "close", "high", "low", "open", "volumefrom", "volumeto"]

    def get_ohlc_full(self, fsym: str, tsym = 'usd'):
        path = f"{self.url}/v2/histoday?fsym={fsym.upper()}&tsym={tsym.upper()}&allData=true"
        data = self.__get_data(path)
        return self.__parse_ohlc(fsym, data)

    def get_ohlc_limit(self, fsym: str, tsym = 'usd', limit = 10):
        path = f"{self.url}/v2/histoday?fsym={fsym.upper()}&tsym={tsym.upper()}&limit={limit}"
        data = self.__get_data(path)
        ohlc_list = self.__parse_ohlc(fsym, data)
        return ohlc_list[len(ohlc_list) - 1] if limit == 1 else ohlc_list
    
    def __parse_ohlc(self, fsym: str, data: dict):
        df = pd.DataFrame(data, columns=self.columns)
        df.rename(columns={"time": "timestamp"}, inplace=True)
        df["symbol"] = fsym
        df["provider"] = "cryptocompare"
        df["datetime"] = pd.to_datetime(df["timestamp"], unit="s")
        df["datetime"] = df["datetime"].dt.strftime('%Y-%m-%d %H:%M:%S')
        return df.to_dict(orient="records")
    
    def __get_data(self, path: str):
        print(f"Llamando a la API: {path}")
        response = requests.get(path)
        if not response.ok:
            print(f"Someting went wrong... {response.content.decode()}")
        data = response.json()
        return data["Data"]["Data"]
