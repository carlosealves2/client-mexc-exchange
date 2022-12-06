from pprint import pprint

from MexcClient import MexcClient


def test_exchange_connection_success():
    client = MexcClient("key", "secret")
    response = client.check_connection()
    assert response is True


def test_collect_server_hour():
    client = MexcClient("key", "secret")
    response = client.server_time()
    assert isinstance(response, dict)
    assert "serverTime" in response
    assert isinstance(response.get("serverTime"), int)


def test_collect_exchange_info():
    client = MexcClient("key", "secret")
    response = client.exchange_info()
    assert isinstance(response, dict)
    assert "symbols" in response
    assert len(response.get("symbols")) > 0


def test_order_book_symbol():
    client = MexcClient("key", "secret")
    response = client.order_book_of_symbol("BTCUSDT")
    assert isinstance(response, dict)
    assert "lastUpdateId" in response
    assert len(response.get("bids")) == 100


def test_collect_recent_trades_of_symbol():
    client = MexcClient("key", "secret")
    response = client.recent_trades_list("BTCUSDT")
    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert "price" in response[0]


def test_collect_old_trade_lookup_of_symbol():
    client = MexcClient("key", "secret")
    response = client.old_trade_lookup("BTCUSDT")
    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert "price" in response[0]
