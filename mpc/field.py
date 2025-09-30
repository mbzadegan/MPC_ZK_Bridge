# Finite field utilities for a safe-ish 61-bit prime (EDU only)
P = 2**61 - 1  # small-ish prime; not cryptographic

def modp(x: int) -> int:
    return x % P

def add(a: int, b: int) -> int:
    return (a + b) % P

def sub(a: int, b: int) -> int:
    return (a - b) % P

def mul(a: int, b: int) -> int:
    return (a * b) % P

def inv(a: int) -> int:
    return pow(a, P - 2, P)
