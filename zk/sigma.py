# Schnorr proof of knowledge of discrete log (toy, EDU ONLY).
from .pedersen import p, g, H

def prove_sk(sk: int):
    y = pow(g, sk, p)
    r = (sk * 17 + 42) % (p-1)  # toy 'random'
    t = pow(g, r, p)
    c = H(g, y, t) % (p-1)
    z = (r + c * sk) % (p-1)
    return {"y": y, "t": t, "c": c, "z": z}

def verify(proof) -> bool:
    y, t, c, z = proof["y"], proof["t"], proof["c"], proof["z"]
    lhs = pow(g, z, p)
    rhs = (t * pow(y, c, p)) % p
    return lhs == rhs
