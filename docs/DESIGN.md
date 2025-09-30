# DESIGN

This repository contains small, readable prototypes for:
- 2PC additive-sharing over a prime field with Beaver-style multiplication.
- Schnorr proof of knowledge via a Sigma protocol + Fiat–Shamir.
- A toy MPC-in-the-Head (MiH) construction for a dot-product relation.

## Security model
- Semi-honest adversaries for MPC (no aborts, no malicious behavior).
- Standard soundness and (honest-verifier) zero-knowledge for Sigma protocols.
- MiH is sketched with commitments to views and Fiat–Shamir challenge; full verification would reconstruct consistency across opened views.

## Correctness
- Unit tests (to add) should check reconstruction and protocol identities.
- Demos print small instances and compare with direct computations.

## Efficiency
- Constant factors matter; profile Python hotspots and replace with Rust or C if needed.
- Communication is simulated; add a simple socket layer for real message costs.
