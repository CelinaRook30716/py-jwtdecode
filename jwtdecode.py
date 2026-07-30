"""Decode a JWT payload (NO signature verification). Standard library only."""
import base64, json


def decode_payload(token):
    parts = token.split(".")
    if len(parts) != 3:
        raise ValueError("not a JWT")
    seg = parts[1]
    seg += "=" * (-len(seg) % 4)
    return json.loads(base64.urlsafe_b64decode(seg))
