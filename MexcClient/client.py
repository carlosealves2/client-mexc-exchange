import requests

from MexcClient.Enums import EnumKlineInterval


class MexcClient:
    def __init__(self, api_key: str, api_secret: str):
        self.__api_key = api_key
        self.__api_secret = api_secret
        self.__base_url = "https://api.mexc.com"

    @property
    def base_url(self) -> str:
        return self.__base_url

    def check_connection(self) -> bool:
        response = requests.get(self.__base_url + "/api/v3/ping")
        return response.ok

    def server_time(self) -> dict:
        response = requests.get(self.__base_url + "/api/v3/time")
        if response.ok:
            return response.json()
        return {
            "error": "An error occurred while trying to collect the time from the server."
        }

    def exchange_info(self):
        response = requests.get(self.__base_url + "/api/v3/exchangeInfo")
        if response.ok:
            return response.json()
        return {
            "error": "An error occurred while trying to collect exchange information."
        }

    def order_book_of_symbol(self, symbol: str, limit: int = 100) -> dict:
        """
        function to collect the order book of a symbol.
        :param symbol: trade pair, example: BTCUSDT
        :param limit: result limit is a range from 100 to a maximum of 5000 results. The default is 100.
        :return: dict
        """
        response = requests.get(
            self.__base_url + "/api/v3/depth", params={"symbol": symbol, "limit": limit}
        )

        if response.ok:
            # response mapping
            # Name	Type	Description
            # lastUpdateId	long	Last Update Id
            # bids	list	Bid [Price, Quantity ]
            # asks	list	Ask [Price, Quantity ]
            return response.json()

        return {"error": f"An error occurred while collecting the {symbol} order book"}

    def recent_trades_list(self, symbol: str, limit: int = 500) -> list:
        """
        this function collects the last transactions of an informed symbol.
        :param symbol: trade pair, example: BTCUSDT
        :param limit: result limit is a range from 500 to a maximum of 1000 results. The default is 500.
        :return: list
        """
        response = requests.get(
            self.__base_url + "/api/v3/trades",
            params={"symbol": symbol, "limit": limit},
        )

        if response.ok:
            # response mapping
            # Name	Description
            # id	Trade id
            # price	Price
            # qty	Number
            # quoteQty	Trade total
            # time	Trade time
            # isBuyerMaker	Was the buyer the maker?
            # isBestMatch	Was the trade the best price match?
            return response.json()

        return [
            "error",
            f"An error occurred when trying to collect the last transactions for the symbol {symbol}.",
        ]

    def old_trade_lookup(self, symbol: str, limit: int = 500) -> list:
        """
        this function collects the last transactions of an informed symbol.
        :param symbol: trade pair, example: BTCUSDT
        :param limit: result limit is a range from 500 to a maximum of 1000 results. The default is 500.
        :return: list
        """
        response = requests.get(
            self.__base_url + "/api/v3/historicalTrades",
            params={"symbol": symbol, "limit": limit},
        )

        if response.ok:
            # response mapping:
            # Name	Description
            # id	Trade id
            # price	Price
            # qty	Number
            # quoteQty	Trade total
            # time	Trade time
            # isBuyerMaker	Was the buyer the maker?
            # isBestMatch	Was the trade the best price match?
            return response.json()

        return [
            "error",
            f"An error occurred while trying to collect the oldest operations for the {symbol} symbol.",
        ]

    def kline_data(
        self,
        symbol: str,
        interval: EnumKlineInterval,
        start_time: int = 0,
        end_time: int = 0,
        limit: int = 500,
    ) -> list:
        """
        function to collect the row of candlesticks of an informed symbol.
        The info receives the name of the symbol, its limit and
        its interval, some optional parameters can also be informed.

        :param symbol: trade pair, example: BTCUSDT
        :param interval: kline interval
        :param start_time: unix time format
        :param end_time: unix time format
        :param limit: result limit is a range from 500 to a maximum of 1000 results. The default is 500.
        :return: list
        """

        params = {"symbol": symbol, "limit": limit, "interval": interval.value}

        if start_time > 0:
            params["startTime"] = start_time

        if end_time > 0:
            params["endTime"] = end_time

        response = requests.get(
            self.__base_url + "/api/v3/historicalTrades",
            params=params,
        )

        if response.ok:
            # response mapping:
            # Index	Description
            # 0	Open time
            # 1	Open
            # 2	High
            # 3	Low
            # 4	Close
            # 5	Volume
            # 6	Close time
            # 7	Quote asset volume
            return response.json()

        return [
            "error",
            f"An error occurred when trying to collect the row of candlesticks for the symbol {symbol}.",
        ]

    def current_average_price(self, symbol: str) -> dict:
        response = requests.get(
            self.__base_url + "/api/v3/avgPrice", params={"symbol": symbol}
        )
        if response.ok:
            # respose mapping
            # Name	Description
            # mins	Average price time frame
            # price	Price
            return response.json()

        return {
            "error": f"An error occurred when trying to collect the average price for the symbol {symbol}."
        }
