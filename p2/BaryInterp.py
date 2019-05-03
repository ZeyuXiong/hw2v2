import numpy as np 

class BaryInterp:

	MAXSIZE = 500

	#initialize the class
	def __init__(self, initpts = np.array([0]), initfval = np.array([1]), **kwarg):		
		self.W = np.ones((self.MAXSIZE,self.MAXSIZE))
		self.pts = np.array([])
		self.fval = np.array([])
		self.update(initpts, initfval, **kwarg)
		if ("cheb1" in kwarg) or ("cheb2" in kwarg):
			return

		self.weights = self.W[len(self.pts)-1]


	#given x, find the interpolated value
	def get_val(self,x):
		fx = 0
		N = len(self.pts)-1
		L = 0
		for j in range(N+1):
			if(abs(x-self.pts[j])<1e-10):
				return self.fval[j]
			L += self.weights[j]/(x-self.pts[j])

		for j in range(N+1):
			fx += self.weights[j]*self.fval[j]/(x-self.pts[j])
		return fx/L

	#adding points and update the weight
	def update(self,newpts = np.array([0]),newfval = np.array([1]),**kwarg):
		if "cheb1" in kwarg:
			self.fval = np.copy(kwarg["cheb1"])
			self.chebweight1(len(self.fval)-1)
			return
		if "cheb2" in kwarg:
			self.fval = np.copy(kwarg["cheb2"])
			self.chebweight2(len(self.fval)-1)
			return


		n = len(self.pts)
		self.pts = np.append(self.pts,newpts)
		self.fval = np.append(self.fval,newfval)
		N = len(self.pts)-1
		for K in range(n,N+1):

			for j in range(K):
				self.W[K][j] = self.W[K-1][j]/(self.pts[j]-self.pts[K])

			self.W[K][K] =1
			for j in range(K):
				self.W[K][K] /= (self.pts[K]-self.pts[j])

		self.weights = self.W[N]


	def chebweight1(self,N):
		self.pts = np.polynomial.chebyshev.chebpts1(N+1)
		j = np.arange(N+1)
		self.weights = (-1)**j * np.sin((2*j+1)*np.pi/2/(N+1))


	def chebweight2(self,N):
		if N == 0:
			self.pts = np.array([0])
		else:
			self.pts = np.polynomial.chebyshev.chebpts2(N+1)
		j = np.arange(N+1)
		self.weights = (-1)**j * 1.0
		self.weights[0] /= 2.
		self.weights[N] /= 2.
		#print("cheb2 called, weights =", self.weights)






