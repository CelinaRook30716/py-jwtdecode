# JWT payload decoder (no verify)

```
jwtdecode.py
```

See the test next to the source for usage.

This is a tiny utility for when you need to look at what's inside a JWT payload without bothering with signature checks. It does base64 decoding only — no verification, no key management, no ceremony. That's a feature, not a bug, because verification is a separate concern and you shouldn't be doing it in the same function that's meant for eyeballing token contents.

There's a real risk here that I want to name outright: if you use this on a token from an untrusted source and then act on the decoded claims as if they were authenticated, you've built yourself a privilege escalation. The payload is just base64 — anyone can forge it. So this is strictly for debugging, logging, or content inspection where the token has already passed verification elsewhere. Don't conflate the two.

The implementation itself is boring on purpose. It splits the token on dots, takes the middle segment, and base64-decodes it with padding handled correctly. No dependencies, no service to run — just the standard library. If you've ever hand-rolled this, you know the padding edge case is where most naive implementations fall over, so that's handled explicitly.

Trade-offs compared to pulling in a full JWT library:

| Approach | Pros | Cons |
|----------|------|------|
| This decoder | Zero dependencies, works offline, trivial to audit | No verification, no error messages from a standards body, you own the edge cases |
| Full JWT library | Verification, algorithm negotiation, ecosystem-tested error paths | Dependency bloat for a one-liner, you inherit its attack surface and version churn |

If you need to verify signatures, reach for a proper library and don't bolt verification onto this. If you just need to see what a token claims, this is enough and it won't surprise you.

Usage is exactly what you'd expect:

```python
import jwt_payload

claims = jwt_payload.decode("eyJhbGciOiJub25lIn0.eyJzdWIiOiIxMjM0In0.abc")
print(claims["sub"])  # "1234"
```

The error handling is minimal: malformed tokens raise a clear exception, and that's intentional. A silent failure here would hide the fact that you're inspecting garbage. Fail loud, look at the token, move on.

One more thing worth saying plainly: this does not validate the `alg` header, does not check expiration, does not care about issuer. All of that is your job at the point where you decide the token is trustworthy. This just decodes.