from zk.sigma import prove_sk, verify
proof = prove_sk(123456789)
print("Proof verifies?", verify(proof))
