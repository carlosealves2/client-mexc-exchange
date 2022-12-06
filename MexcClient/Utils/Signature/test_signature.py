import urllib.parse

from MexcClient.Utils.Signature.signature import generate_signature


def test_create_a_valid_signature_hash():
    params = {"params1": "hash", "params2": "test", "params3": "limit"}
    size = 64

    str_params = urllib.parse.urlencode(params)
    str_hash = generate_signature("secret".encode(), str_params.encode())

    assert len(str_hash) == size
