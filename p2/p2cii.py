import numpy as np 
import matplotlib.pyplot as plt
from BaryInterp import BaryInterp


f = lambda x: 1./(1+25*x*x)

for n in [4,8,16]:
	x = np.linspace(-1,1,n)
	Pn = BaryInterp(x,f(x))

	err = np.zeros(1001)
	xref = np.linspace(-1,1,1001)
	for i in range(1001):
		err[i] = (Pn.get_val(xref[i])-f(xref[i]))/f(xref[i])
	plt.plot(xref,err)
	print("error of", n, "nodes:",np.max(abs(err)))
plt.legend(["4 nodes", "8 nodes", "16 nodes"])
plt.show()


