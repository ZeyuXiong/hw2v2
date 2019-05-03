import numpy as np 
from scipy.fftpack import dct 


def chebcoeffs(fval):
	N = len(fval)-1
	coeffs = dct(fval,type = 1)/N
	coeffs[0] /= 2
	coeffs[N] /= 2
	return coeffs