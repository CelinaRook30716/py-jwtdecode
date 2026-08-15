# JWT payload decoder (no verify)

```
jwtdecode.py
```
Keep the Python Jwtdecode test alongside the implementation if you want concrete examples to read.

This utility decodes a JWT payload for inspection. It is base64 only and performs no signature verification, so do not trust the contents as authenticated. Anyone can forge a token; you are merely looking at what was encoded.

Python Jwtdecode relies solely on the python standard library. There is no service to stand up and no dependency to install, which keeps the failure surface small but means you must handle malformed input yourself.