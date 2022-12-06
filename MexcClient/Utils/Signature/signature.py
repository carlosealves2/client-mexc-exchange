import hashlib
import hmac


def generate_signature(secret, str_params) -> str:
    return hmac.new(secret, msg=str_params, digestmod=hashlib.sha256).hexdigest()
