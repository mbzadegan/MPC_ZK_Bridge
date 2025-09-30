# MPC–ZK Bridge
*A minimal, teachable codebase that bridges Secure Multi‑Party Computation (MPC) and Zero‑Knowledge (ZK).*

This repository provides **small, readable Python prototypes** of core primitives:
- **MPC (2PC, semi‑honest)** using additive secret sharing over a prime field with **Beaver‑style secure multiplication**.
- **ZK foundations**: a toy **Pedersen‑style commitment**, a **Schnorr Σ‑protocol** (with Fiat–Shamir), and a lightweight **MPC‑in‑the‑Head (MiH)** proof for a dot‑product relation.
- **Examples** you can run in seconds. No external dependencies (pure Python stdlib).

> ⚠️ **Security Scope:** This is for **education and research prototyping only** (tiny moduli, toy PRG, semi‑honest model, no network adversary). **Do not use in production.**

---

## Contents
```
mpc-zk-bridge/
├── mpc/
│   ├── field.py         # finite field arithmetic modulo a small prime (EDU only)
│   ├── sharing.py       # additive secret sharing, reconstruction, share addition
│   ├── beaver.py        # toy Beaver triples + secure multiplication over shares
│   ├── protocols.py     # example: secret-shared dot product (CLI-capable)
│   └── __init__.py
├── zk/
│   ├── pedersen.py      # toy Pedersen-style commitment (hash/exp mod small p)
│   ├── sigma.py         # Schnorr proof of knowledge + Fiat–Shamir transform
│   ├── mih.py           # MPC-in-the-Head proof for <x,w>=y (toy verification)
│   └── __init__.py
├── examples/
│   ├── demo_mpc_dot.py      # runs a private dot product via 2PC + Beaver
│   ├── demo_zk_schnorr.py   # proves knowledge of discrete log (toy)
│   └── demo_mih_dot.py      # produces a MiH proof for dot-product relation
├── docs/
│   ├── DESIGN.md        # security model, correctness notes, efficiency remarks
│   └── ROADMAP.md       # ideas for PQ, malicious security, and engineering work
├── LICENSE
├── requirements.txt     # intentionally empty (stdlib-only)
└── README.md            # you are here
```

---

## Quickstart
Tested with Python 3.10+.
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt   # (no packages; keeps reviewers' setup trivial)

# 1) MPC demo: secret dot product
python examples/demo_mpc_dot.py

# 2) ZK demo: Schnorr proof of knowledge (toy, Fiat–Shamir)
python examples/demo_zk_schnorr.py

# 3) ZK demo: MPC-in-the-Head proof for <x,w>=y
python examples/demo_mih_dot.py
```

### Minimal CLIs
`protocols.py` exposes a tiny CLI for the MPC dot product:
```bash
python -m mpc.protocols --x 1,2,3 --y 4,5,6 --seed 42
# -> prints dot(x,y) mod p
```

---

## What each file does (deeper)
### `mpc/field.py`
- Defines a small prime modulus `P = 2**61 - 1` and basic ops: `add`, `sub`, `mul`, `inv`, `modp`.
- Small prime keeps arithmetic fast and code readable. Not cryptographic strength.

### `mpc/sharing.py`
- **`share_secret(x, r)`**: deterministic 2‑party additive sharing of `x` using randomizer `r`.
- **`reconstruct(s1, s2)`**: recombines two shares to the original value (mod `P`).
- **`add_shares`**: homomorphic addition on shares.

### `mpc/beaver.py`
- **BeaverTriple(a,b)** with `c=a*b mod P`.
- **`triple_from_seed(seed)`**: deterministic toy PRG makes simple correlated randomness for testing.
- **`secure_mul(x1,x2,y1,y2,T)`**: computes shares of `x*y` using a Beaver triple `T`.

### `mpc/protocols.py`
- **`dot_product(x,y, seed)`**: secret‑shares inputs, multiplies element‑wise via Beaver, sums, and reconstructs.
- CLI wrapper so reviewers can run it without opening code.

### `zk/pedersen.py`
- Toy Pedersen‑style commitment `C = g^m h^r (mod p)` with a tiny unsafe modulus. Educational placeholder.

### `zk/sigma.py`
- **Schnorr Σ‑protocol** to prove knowledge of `sk` with public key `y=g^sk`.
- **`prove_sk(sk)`** → dict with `(y,t,c,z)`; **`verify(proof)`** checks `g^z = t * y^c` (mod `p`).
- Fiat–Shamir used to derive challenge `c` from a hash → makes it NIZK‑like in the toy model.

### `zk/mih.py`
- **MPC‑in‑the‑Head** sketch for a dot‑product relation: prover commits to three simulated party views; verifier opens two (per Fiat–Shamir challenge) and checks structural consistency (toy check here).

### `examples/*.py`
- Small scripts that exercise each protocol end‑to‑end and print results for fast review.

### `docs/*.md`
- **DESIGN.md**: security model (semi‑honest), correctness notes, efficiency commentary.
- **ROADMAP.md**: next steps for post‑quantum replacements, malicious security (SPDZ‑style MACs, sacrifices), and engineering (networking, benchmarking, fuzzing).

---

## Typical outputs
- `demo_mpc_dot.py`: prints the secret dot product under the small prime field.
- `demo_zk_schnorr.py`: prints `Proof verifies? True/False`.
- `demo_mih_dot.py`: prints whether the toy MiH proof passes the basic structural check.

---

## Extending the repo (good first issues)
- Add **unit tests**: share/reconstruct identities, Beaver soundness checks, Σ‑protocol completeness.
- Replace toy parameters with larger primes and add **benchmarks**.
- Add a tiny **socket transport** for 2PC to measure real communication.
- Explore **PQ‑friendly** commitments and **OT‑based** multiplication for MPC.
- Strengthen MiH verification to re‑execute the opened views and consistency constraints.

---

## License
MIT — see `LICENSE`.
