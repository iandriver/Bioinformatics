import itertools as iter
from math import factorial as fac

def part_p(n,k):
	result = 0
	for y in range(k, n+1):
		len_combs = fac(n)/(fac(n-y)*fac(y))
		result+=len_combs

	print result%1000000
	
part_p(1688,845)		