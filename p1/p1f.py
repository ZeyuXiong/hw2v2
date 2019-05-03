import numpy as np 
import matplotlib.pyplot as plt
from BaryInterp import BaryInterp


f = lambda x: x**4 + 2*x*x*x + 3*x*x + 4*x + 5
#f = lambda x: np.polyval([1, 2, 3, 4, 5], x)
pts = np.linspace(-1,1,5)
P1 = BaryInterp(pts,f(pts))

k = np.arange(0,5,1)
pts = np.cos((2*k*np.pi+np.pi)/10)
P2 = BaryInterp(pts,f(pts))

pts = np.cos(k*np.pi/4)
P3 = BaryInterp(pts,f(pts))

N=20001
xref = np.linspace(-1,1,N)
err1 = np.zeros(N)
err2 = np.zeros(N)
err3 = np.zeros(N)
for i in range(N):
	err1[i] = ( P1.get_val(xref[i])-f(xref[i]) )/f(xref[i])
	err2[i] = ( P2.get_val(xref[i])-f(xref[i]) )/f(xref[i])
	err3[i] = ( P3.get_val(xref[i])-f(xref[i]) )/f(xref[i])
plt.plot(xref,err1,xref,err2,xref,err3)
plt.legend(['linspace','roots of T5(x)','extrema of T4(x)'])
plt.show()

print("error of linspace:", np.max(abs(err1)))
print("error of roots of T5(x):", np.max(abs(err2)))
print("error of extrema of T4(x):", np.max(abs(err3)))
