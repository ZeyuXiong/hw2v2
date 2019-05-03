import numpy as np 
import timeit


setup = '''def firstn(n):
	num = 0
	while num < n:
		yield num
		num += 1

sum_of_first_n = sum(firstn(1000000))'''
print(timeit.timeit(setup + '''
print(sum_of_first_n)''',number=1000))