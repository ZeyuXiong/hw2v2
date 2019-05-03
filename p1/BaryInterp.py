import numpy as np 

class BaryInterp:

	MAXSIZE = 20

	def __init__(self, initpts, initfval):
		self.W = np.ones((self.MAXSIZE,self.MAXSIZE))
		self.W[0][0] = 1
		self.pts = np.copy(initpts)
		self.fval = np.copy(initfval)
		for K in range(1,len(initpts)):
			for j in range(K):
				self.W[K][j] = self.W[K-1][j]/(initpts[j]-initpts[K])

			self.W[K][K] =1
			for j in range(K):
				self.W[K][K] /= (initpts[K]-initpts[j])
		#self.W[K] = 1/self.W[K]

	def get_val(self,x):
		fx = 0
		N = len(self.pts)-1
		L = 1
		for j in range(N+1):
			if(x == self.pts[j]):
				return self.fval[j]
			L *= (x-self.pts[j])

		for j in range(N+1):
			fx += self.W[N][j]*self.fval[j]/(x-self.pts[j])
		return fx*L

	def update(self,newpts,newfval):
		N = len(self.pts)
		self.pts = np.append(self.pts,newpts)
		self.fval = np.append(self.fval,newfval)
		for K in range(N,len(self.pts)):
			for j in range(K):
				self.W[K][j] = self.W[K-1][j]*(initpts[j]-initpts[K])

			self.W[K][K] =1
			for j in range(K):
				self.W[K][K] *= (initpts[K]-initpts[j])





