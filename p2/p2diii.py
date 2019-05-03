import numpy as np 
import matplotlib.pyplot as plt
from BaryInterp import BaryInterp


f = lambda x: np.cosh(x)

N = 2**np.arange(9)
E_infty = np.zeros(len(N))
for j in range(len(N)):
	n = N[j] 
	if n == 1:
		x = np.array([0])
	else:
		x = np.polynomial.chebyshev.chebpts2(n)
	Pn = BaryInterp(cheb2=f(x))


	err = np.zeros(10001)
	xref = np.linspace(-1,1,10001)
	for i in range(10001):
		err[i] = Pn.get_val(xref[i])-f(xref[i])
	
	E_infty[j] = np.max(abs(err))

plt.figure(1)
plt.semilogy(N,E_infty,'.')
plt.xlabel("N+1")
plt.ylabel("error of cosh(x)")
#plt.legend(["max error", "1st order reference"])

f = lambda x: np.exp(-x*x)

for j in range(len(N)):
	n = N[j] 
	if n == 1:
		x = np.array([0])
	else:
		x = np.polynomial.chebyshev.chebpts2(n)
	Pn = BaryInterp(cheb2=f(x))


	err = np.zeros(10001)
	xref = np.linspace(-1,1,10001)
	for i in range(10001):
		err[i] = Pn.get_val(xref[i])-f(xref[i])
	
	E_infty[j] = np.max(abs(err))
plt.figure(2)
plt.semilogy(N,E_infty,'.')
plt.xlabel("N+1")
plt.ylabel("error of exp(-x*x)")
#plt.legend(["max error", "3rd order reference"])


f = lambda x: np.cos(100*np.pi*x)
N *= 16
for j in range(len(N)):
	n = N[j] 
	if n == 1:
		x = np.array([0])
	else:
		x = np.polynomial.chebyshev.chebpts2(n)
	Pn = BaryInterp(cheb2=f(x))


	err = np.zeros(10001)
	xref = np.linspace(-1,1,10001)
	for i in range(10001):
		err[i] = Pn.get_val(xref[i])-f(xref[i])
	
	E_infty[j] = np.max(abs(err))

plt.figure(3)
plt.semilogy(N,E_infty,'.')
plt.xlabel("N+1")
plt.ylabel("error of cos(100*pi*x)")
#plt.legend(["max error", "5th order reference"])
plt.show()




