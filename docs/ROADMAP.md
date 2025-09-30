# ROADMAP

1. **Post-Quantum (PQ) track**
   - Replace discrete-log groups with hash-/lattice-based commitments.
   - Explore MiH with PQ-friendly components; analyze proof sizes.
   - Swap 2PC multiplication to OT-based (IKNP) over appropriate rings.

2. **Active security**
   - Add MACs / sacrifice steps (SPDZ-style) and malicious checks.
   - Consistency proofs for shares; ZK proofs for correct openings.

3. **Applications**
   - Private linear models: secure inference for tiny networks (ReLU via polynomial approximations).
   - Verifiable MPC: ZK proof that outputs are from a valid MPC execution.

4. **Engineering**
   - Add property tests and fuzzers.
   - Add a minimal network layer and measure comms latency/bandwidth.
