from math import factorial as fac
def mend_prob(gen, num):
	prog = 2**gen  						# number of progeny in that generation
	result = 0
	for x in range(num, prog+1):		#sum the cumulative probability of exactly num or greater individuals occuring
		result += ((fac(prog)/(fac(x)*fac(prog-x)))*.25**x*.75**(prog-x))
										#formula for binomial probability 
	return ("%.3f" % result)			#round to 3 decimal places
print mend_prob(5, 8)		
			