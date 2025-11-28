# Minimal Pedersen-like commitment in a toy group (Education ONLY).
from hashlib import sha256

# Tiny toy modulus; DO NOT USE for real security.
p = (1 << 127) - 1
g = 5
h = 7  # independent generator in real settings

def H(*vals) -> int:
    m = sha256()
    for v in vals:
        if isinstance(v, int):
            m.update(v.to_bytes(64, "big", signed=False))
        else:
            m.update(str(v).encode())
    return int.from_bytes(m.digest(), "big")

def commit(m: int, r: int) -> int:
    return pow(g, m, p) * pow(h, r, p) % p
