# Simple MPC protocols built from sharing + Beaver.
import argparse
from .field import modp, add, mul
from .sharing import share_secret, reconstruct, add_shares
from .beaver import triple_from_seed, secure_mul

def dot_product(x, y, seed=42):
    assert len(x) == len(y)
    shares_x = [share_secret(int(xi), seed + i) for i, xi in enumerate(x)]
    shares_y = [share_secret(int(yi), seed + 1000 + i) for i, yi in enumerate(y)]
    z1 = 0
    z2 = 0
    for i, ((x1, x2), (y1, y2)) in enumerate(zip(shares_x, shares_y)):
        T = triple_from_seed(seed + 2000 + i)
        w1, w2 = secure_mul(x1, x2, y1, y2, T)
        z1 = add(z1, w1); z2 = add(z2, w2)
    return reconstruct(z1, z2)

def main():
    ap = argparse.ArgumentParser(description="Toy MPC dot-product via additive shares + Beaver triples.")
    ap.add_argument("--x", type=str, default="1,2,3")
    ap.add_argument("--y", type=str, default="4,5,6")
    ap.add_argument("--seed", type=int, default=42)
    args = ap.parse_args()
    x = [int(t) for t in args.x.split(",")]
    y = [int(t) for t in args.y.split(",")]
    res = dot_product(x, y, args.seed)
    print("dot(x,y) mod p =", res)

if __name__ == "__main__":
    main()
