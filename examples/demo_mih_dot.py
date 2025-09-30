from zk.mih import mih_prove, mih_verify
x = [3, 1, 4]; w = [2, 7, 1]; y = 3*2 + 1*7 + 4*1
pi = mih_prove(x, w, y)
print("MiH proof (toy) verifies?", mih_verify(pi))
