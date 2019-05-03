import numpy as np 
from p3a import chebcoeffs
import timeit



setup1 = '''
import numpy as np 
from p3a import chebcoeffs

f = lambda x: np.exp(-x*x)
'''

setup2 = '''
j = np.arange(N+1)
x = np.cos(j*np.pi/N)
An=chebcoeffs(f(x))
'''

print(timeit.timeit(setup1+'''N = 8'''+setup2, number = 10))
print(timeit.timeit(setup1+'''N = 2**13-1'''+setup2, number = 10))
print(timeit.timeit(setup1+'''N = 2**13'''+setup2, number = 10))
print(timeit.timeit(setup1+'''N = 2**17-1'''+setup2, number = 10))
print(timeit.timeit(setup1+'''N = 2**17'''+setup2, number = 10))
