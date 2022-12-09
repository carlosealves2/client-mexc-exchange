# Client MEXC Exchange

A simple python client for the [MEXC](https://www.mexc.com/) exchange. 
Open, unofficial project, intended to consume all endpoints provided by Exchange 
[documentation](https://mxcdevelop.github.io/apidocs/spot_v3_en/#introduction).

## Summary

* [Pypi](#pypi)
* [Dependencies](#dependencies)
* [how to use](#how-to-use)
* [functions implemented so far](#functions-implemented-so-far)
* [Instalation](#installation)
  * [Python version](#python-version)

## Pypi
see the project on Pypi by accessing the [link](https://pypi.org/project/mexcapiclient/).

## Dependencies

This project uses some libraries for its operation as well as tests and linter for code organization. Its dependencies are:

* [Requests](https://requests.readthedocs.io/en/latest/)
* [Black](https://github.com/psf/black)
* [Pytest](https://docs.pytest.org/en/7.1.x/contents.html)

## how to use 

A simple code example for client use is:

    from MexcClient.client import MexcClient

    client = MexcClient("API_KEY", "API_SECRET")
    client.server_time()

## functions implemented so far

| Func                                | Method | Endpoint                 | Params                                                                                                                                                                   | Section               |
|-------------------------------------|--------|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------|
| check_connection                    | GET    | /api/v3/ping             | None                                                                                                                                                                     | Market Data Endpoints |
| server_time                         | GET    | /api/v3/time             | None                                                                                                                                                                     | Market Data Endpoints |
| exchange_info                       | GET    | /api/v3/exchangeInfo     | None                                                                                                                                                                     | Market Data Endpoints |
| order_book_of_symbol                | GET    | /api/v3/depth            | symbol: str, limit: int                                                                                                                                                  | Market Data Endpoints |
| recent_trades_list                  | GET    | /api/v3/trades           | symbol: str, limit: int                                                                                                                                                  | Market Data Endpoints |
| old_trade_lookup                    | GET    | /api/v3/historicalTrades | symbol: str, limit: int                                                                                                                                                  | Market Data Endpoints |
| kline_data                          | GET    | /api/v3/klines           | symbol: str, interval: EnumKlineInterval, start_time: int, end_time: int, limit: int = 500                                                                               | Market Data Endpoints |
| current_average_price               | GET    | /api/v3/avgPrice         | symbol: str                                                                                                                                                              | Market Data Endpoints |
| create_order_test                   | POST   | /api/v3/order/test       | symbol: str, side: EnumOrderSide, _type: EnumOrderType, timestamp: int, quantity: str, quote_order_quantity: str, price: str, new_client_order_id: str, recv_window: int | Spot Account/Trade    |
| create_new_order                    | POST   | /api/v3/order            | symbol: str, side: EnumOrderSide, _type: EnumOrderType, timestamp: int, quantity: str, quote_order_quantity: str, price: str, new_client_order_id: str, recv_window: int | Spot Account/Trade    |
| load_balances                       | GET    | /api/v3/account          | None                                                                                                                                                                     | Spot Account/Trade    |
| load_balance_by_symbol              | GET    | /api/v3/account          | symbol: str                                                                                                                                                              | Spot Account/Trade    |
| cancel_order                        | DELETE | /api/v3/order            | symbol: str, order_id: str, timestamp: int                                                                                                                               | Spot Account/Trade    |
| cancel_all_open_orders_on_a_symbol  | DELETE | /api/v3/openOrders       | symbols: list, timestamp: int                                                                                                                                            | Spot Account/Trade    |


## installation
To install just run the following command:

    pip install mexcapiclient


### Python version
python version used in this project was:

* [Python3.9](https://www.python.org/)

