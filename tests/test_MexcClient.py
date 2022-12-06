from MexcClient.main import MexcClient


def test_exchange_connection_success():
    client = MexcClient("key", "secret")
    response = client.check_connection()
    assert response == True
