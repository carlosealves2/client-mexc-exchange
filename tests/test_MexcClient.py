from MexcClient.main import MexcClient


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
