import numpy as np 
import matplotlib.pyplot as plt
from BaryInterp import BaryInterp


f = lambda x: 1/(1+25*x*x)

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
plt.ylabel("error of 1/(1+25*x*x)")
#plt.legend(["max error", "1st order reference"])

f = lambda x: np.sqrt(x+3)

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
plt.ylabel("error of sqrt(x+3)")
#plt.legend(["max error", "3rd order reference"])


f = lambda x: np.tan(x)

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
plt.ylabel("error of tan(x)")
#plt.legend(["max error", "5th order reference"])
plt.show()




