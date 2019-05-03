import numpy as np 
from p3a import chebcoeffs
import timeit
import time


f = lambda x: np.exp(-x*x)


for N in [2**10-1, 2**13-1, 2**13, 2**17-1, 2**17]:
	start = time.time()
	j = np.arange(N+1)
	x = np.cos(j*np.pi/N)
	An=chebcoeffs(f(x))
	end = time.time()
	print("N =", N, ", t =",end-start)
