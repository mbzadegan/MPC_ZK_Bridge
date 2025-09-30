# MPC-in-the-Head (MiH) ZK proof for a dot-product relation <x,w>=y (toy).
from hashlib import sha256
from .sigma import H
from ..mpc.field import P as Pmod, add, mul, modp

def commit_bytes(b: bytes) -> bytes:
    return sha256(b).digest()

def share3(v: int, r1: int, r2: int):
    s1 = modp(r1); s2 = modp(r2)
    s3 = modp(v - s1 - s2)
    return s1, s2, s3

def mih_prove(x, w, y, seed=123):
    x_sh = [share3(int(xi), seed+i, seed+1000+i) for i, xi in enumerate(x)]
    w_sh = [share3(int(wi), seed+2000+i, seed+3000+i) for i, wi in enumerate(w)]
    views = []
    for party in range(3):
        acc = 0
        transcript = bytearray()
        for i in range(len(x)):
            xi = x_sh[i][party]
            wi = w_sh[i][party]
            acc = add(acc, mul(xi, wi))
            transcript += f"{party}:{i}:{xi}:{wi}:{acc}\n".encode()
        views.append(commit_bytes(bytes(transcript)))
    c = H(*views) % 3  # 0,1,2
    open_idx = [(c+1)%3, (c+2)%3]
    opened = {i: views[i] for i in open_idx}
    return {"views_commit": [v.hex() for v in views], "opened": {k: v.hex() for k,v in opened.items()}, "y": int(y)}

def mih_verify(proof) -> bool:
    return len(proof.get("opened", {})) == 2
