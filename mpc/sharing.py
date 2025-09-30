# 2-party additive secret sharing over F_p (semi-honest, no comms layer).
from .field import modp, add, sub

# Split x into two shares (s1, s2) s.t. s1 + s2 = x (mod p).
def share_secret(x: int, r: int) -> tuple[int, int]:
    s1 = modp(r)
    s2 = sub(x, s1)
    return s1, s2

def reconstruct(s1: int, s2: int) -> int:
    return add(s1, s2)

def add_shares(a1: int, a2: int, b1: int, b2: int) -> tuple[int, int]:
    return add(a1, b1), add(a2, b2)
