class MexcClient:
    def __init__(self, api_key: str, api_secret: str):
        self.__api_key = api_key
        self.__api_secret = api_secret
        self.__base_url = "https://api.mexc.com"

    @property
    def base_url(self) -> str:
        return self.__base_url
