import numpy as np 
from p3a import chebcoeffs


f = lambda x: 8*x**4 + 4*x**3 + 2*x*x + x + 1

j = np.arange(5)
x = np.cos(j*np.pi/4)

print(chebcoeffs(f(x)))