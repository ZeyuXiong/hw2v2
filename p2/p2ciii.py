import numpy as np 
import matplotlib.pyplot as plt
from BaryInterp import BaryInterp


f = lambda x: np.exp(x) #1./(1+25*x*x)

print("chebyshev first kind: ")
for n in [4,8,16]:
	x = np.polynomial.chebyshev.chebpts1(n)
	Pn = BaryInterp(cheb1=f(x))


	err = np.zeros(1001)
	xref = np.linspace(-1,1,1001)
	for i in range(1001):
		err[i] = (Pn.get_val(xref[i])-f(xref[i]))/f(xref[i])
	plt.plot(xref,err)
	print("error of", n, "nodes:",np.max(abs(err)))

plt.legend(["4 nodes", "8 nodes", "16 nodes"])
plt.show()


print("chebyshev second kind: ")
for n in [4,8,16]:
	x = np.polynomial.chebyshev.chebpts2(n)
	Pn = BaryInterp(cheb2=f(x))
	P = BaryInterp(x,f(x))
	#print(Pn.weights, P.weights)


	err = np.zeros(1001)
	xref = np.linspace(-1,1,1001)
	for i in range(1001):
		err[i] = (Pn.get_val(xref[i])-f(xref[i]))/f(xref[i])
	plt.plot(xref,err)
	print("error of", n, "nodes:",np.max(abs(err)))
plt.legend(["4 nodes", "8 nodes", "16 nodes"])
plt.show()


