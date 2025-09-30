# Toy Beaver triples for secure multiplication (EDU only).
from .field import modp, add, sub, mul

class BeaverTriple:
    def __init__(self, a: int, b: int):
        self.a = modp(a)
        self.b = modp(b)
        self.c = mul(self.a, self.b)

def prg(seed: int) -> int:
    # Tiny xorshift-like PRG; deterministic for tests.
    x = (seed ^ 0x9E3779B97F4A7C15) & ((1<<64)-1)
    x ^= (x << 13) & ((1<<64)-1); x ^= (x >> 7); x ^= (x << 17) & ((1<<64)-1)
    return x

def triple_from_seed(seed: int) -> BeaverTriple:
    a = prg(seed) % (2**61 - 1)
    b = prg(seed ^ 0xA5A5) % (2**61 - 1)
    return BeaverTriple(a, b)

def secure_mul(x1, x2, y1, y2, T: BeaverTriple):
    # Given shares x=(x1,x2), y=(y1,y2) and Beaver triple T=(a,b,c), compute shares of z=x*y.
    d = sub(add(x1, x2), T.a)  # open d = x - a
    e = sub(add(y1, y2), T.b)  # open e = y - b
    z = add(T.c, add(mul(d, T.b), add(mul(e, T.a), mul(d, e))))
    # Deterministic re-share for demo
    z1 = modp(d + 1234567)
    z2 = sub(z, z1)
    return z1, z2
