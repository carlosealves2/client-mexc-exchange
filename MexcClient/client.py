import urllib.parse

import requests

from MexcClient.Enums import EnumKlineInterval, EnumOrderSide, EnumOrderType
from MexcClient.Utils.Signature import generate_signature


class MexcClient:
    def __init__(self, api_key: str, api_secret: str):
        self.__api_key = api_key
        self.__api_secret = api_secret
        self.__base_url = "https://api.mexc.com"

    @property
    def base_url(self) -> str:
        return self.__base_url

    def check_connection(self) -> bool:
        return requests.get(self.__base_url + "/api/v3/ping").json() == {}

    def server_time(self) -> dict:
        return requests.get(self.__base_url + "/api/v3/time").json()

    def exchange_info(self):
        return requests.get(self.__base_url + "/api/v3/exchangeInfo").json()

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

        # response mapping
        # Name	Type	Description
        # lastUpdateId	long	Last Update Id
        # bids	list	Bid [Price, Quantity ]
        # asks	list	Ask [Price, Quantity ]
        return response.json()

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

    def current_average_price(self, symbol: str) -> dict:
        response = requests.get(
            self.__base_url + "/api/v3/avgPrice", params={"symbol": symbol}
        )
        # respose mapping
        # Name	Description
        # mins	Average price time frame
        # price	Price
        return response.json()

    def create_order_test(
        self,
        symbol: str,
        side: EnumOrderSide,
        _type: EnumOrderType,
        timestamp: int,
        quantity: str,
        quote_order_quantity: str = None,
        price: str = None,
        new_client_order_id: str = None,
        recv_window: int = None,
    ) -> dict:
        params = {
            "symbol": symbol,
            "side": side.value,
            "type": _type.value,
            "quantity": quantity,
            "recvWindow": 60000,
            "timestamp": timestamp * 1000,
        }

        headers = {"X-MEXC-APIKEY": self.__api_key, "Content-Type": "application/json"}

        if quantity > 1:
            params["quantity"] = quantity

        if quote_order_quantity:
            params["quoteOrderQty"] = quote_order_quantity

        if price:
            params["price"] = price.replace(",", ".")

        if new_client_order_id:
            params["newClientOrderId"] = new_client_order_id

        if recv_window:
            params["recvWindow"] = recv_window

        str_params = urllib.parse.urlencode(params)
        signature = generate_signature(self.__api_secret.encode(), str_params.encode())

        params["signature"] = signature

        response = requests.post(
            self.__base_url + "/api/v3/order/test", headers=headers, params=params
        )

        return response.json()

    def create_new_order(
        self,
        symbol: str,
        side: EnumOrderSide,
        _type: EnumOrderType,
        timestamp: int,
        quantity: str,
        quote_order_quantity: str = None,
        price: str = None,
        new_client_order_id: str = None,
        recv_window: int = None,
    ) -> dict:
        params = {
            "symbol": symbol,
            "side": side.value,
            "type": _type.value,
            "quantity": quantity,
            "recvWindow": 60000,
            "timestamp": timestamp * 1000,
        }

        headers = {"X-MEXC-APIKEY": self.__api_key, "Content-Type": "application/json"}

        if quote_order_quantity:
            params["quoteOrderQty"] = quote_order_quantity

        if price:
            params["price"] = price.replace(",", ".")

        if new_client_order_id:
            params["newClientOrderId"] = new_client_order_id

        if recv_window:
            params["recvWindow"] = recv_window

        str_params = urllib.parse.urlencode(params)
        signature = generate_signature(self.__api_secret.encode(), str_params.encode())

        params["signature"] = signature

        response = requests.post(
            self.__base_url + "/api/v3/order", headers=headers, params=params
        )

        return response.json()
