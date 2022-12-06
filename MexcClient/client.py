import requests


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

    def order_book_of_symbol(self, symbol: str, limit: int = 100):
        """
        function to collect the order book of a symbol.
        :param symbol: trade pair, example: BTCUSDT
        :param limit: result limit is a range from 100 to a maximum of 5000 results. The default is 100.
        :return:
        """
        response = requests.get(
            self.__base_url + "/api/v3/depth", params={"symbol": symbol, "limit": limit}
        )

        if response.ok:
            return response.json()

        return {"error": f"An error occurred while collecting the {symbol} order book"}
