import numpy as np 
import matplotlib.pyplot as plt
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

#setN = ['''N = 2**10''']
N = []
runtime = []
for k in range(10,26,2):
	runtime.append(timeit.timeit(setup1+'''N = 2**'''+str(k)+setup2, number = 10))
	N.append(float(2**k))
plt.loglog(N,runtime,'.')
plt.loglog(N,np.array(N)/2**20)
plt.loglog(N,np.array(N)**2/2**20)
plt.legend(["runtime vs N", "1st-order reference", "2nd-order reference"])
plt.show()