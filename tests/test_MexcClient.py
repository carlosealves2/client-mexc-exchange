from datetime import datetime

import pytest

from MexcClient import MexcClient
from MexcClient.Enums import EnumKlineInterval
from MexcClient.Enums.enums import EnumOrderSide, EnumOrderType


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


def test_collect_candle_data_of_symbol():
    client = MexcClient("key", "secret")
    response = client.kline_data("BTCUSDT", EnumKlineInterval.ONE_MIN)
    assert isinstance(response, list)
    assert isinstance(response[0], dict)


def test_get_current_average_price():
    client = MexcClient("key", "secret")
    response = client.current_average_price("BTCUSDT")
    assert isinstance(response, dict)
    assert "price" in response
    assert isinstance(response.get("mins"), int)


@pytest.mark.skip(
    reason="Sensitive credentials are required in this test and cannot be exposed."
)
def test_create_new_order_test():
    client = MexcClient("test", "test")
    timestamp = datetime.now().timestamp()

    response = client.create_order_test(
        "BTCUSDT",
        EnumOrderSide.SELL,
        EnumOrderType.MARKET,
        int(timestamp),
        "12000",
        price="2334",
    )

    assert isinstance(response, dict)
    assert response == {}


@pytest.mark.skip(
    reason="Sensitive credentials are required in this test and cannot be exposed."
)
def test_get_account_information_returning_dict_no_empty():
    client = MexcClient("test", "test")
    result = client._load_account_info()
    assert isinstance(result, dict)
    assert result != {}
    assert "balances" in result


@pytest.mark.skip(
    reason="Sensitive credentials are required in this test and cannot be exposed."
)
def test_load_only_balances_for_account():
    client = MexcClient("test", "test")
    result = client.load_balances()
    assert isinstance(result, list)
    assert result != []


@pytest.mark.skip(
    reason="Sensitive credentials are required in this test and cannot be exposed."
)
def test_load_balance_and_filter_result_by_symbol():
    client = MexcClient("test", "test")
    result = client.load_balance_by_symbol("USDT")
    assert isinstance(result, dict)
    assert result != {}
    assert "asset" in result
    assert result.get("asset") == "USDT"


@pytest.mark.skip(
    reason="Sensitive credentials are required in this test and cannot be exposed."
)
def test_cancel_order():
    client = MexcClient("test", "test")
    ts = int(datetime.now().timestamp())
    created_order = client.create_new_order(
        "BIT1USDT",
        EnumOrderSide.BUY,
        EnumOrderType.LIMIT,
        ts,
        "1300000",
        price="0.000005",
    )

    assert created_order
    assert created_order.get("symbol")
    assert created_order.get("orderId")

    ts = int(datetime.now().timestamp())
    deleted_order = client.cancel_order(
        created_order.get("symbol"), created_order.get("orderId"), ts
    )

    assert deleted_order
    assert deleted_order.get("symbol")
    assert deleted_order.get("orderId")

@pytest.mark.skip(
    reason="Sensitive credentials are required in this test and cannot be exposed."
)
def test_delete_all_orders_open_on_a_symbol():
    client = MexcClient("test", "test")

    for _ in range(5):
        ts = int(datetime.now().timestamp())
        client.create_new_order(
            "BIT1USDT",
            EnumOrderSide.BUY,
            EnumOrderType.LIMIT,
            ts,
            "1300000",
            price="0.000005",
        )

    ts = int(datetime.now().timestamp())
    canceled_orders = client.cancel_all_open_orders_on_a_symbol(["BIT1USDT"], ts)
    assert canceled_orders
    assert canceled_orders != []
