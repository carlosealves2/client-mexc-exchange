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
        return {"error": "An error occurred while trying to collect the time from the server."}
