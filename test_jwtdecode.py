import base64, json
from jwtdecode import decode_payload


def test_decode():
    payload = base64.urlsafe_b64encode(json.dumps({"sub": "42"}).encode()).rstrip(b"=").decode()
    assert decode_payload("h." + payload + ".s") == {"sub": "42"}
