from math import log
from math import factorial as fac
import sys

def log_prob(seq, GC_prob):
	prob_dict ={'A':(1-GC_prob)/2, 'T':(1-GC_prob)/2, 'C':GC_prob/2, 'G':GC_prob/2}
	prob = log(prob_dict[seq[0]], 10)
	for nuc in seq[1:]:
		prob1 = log(prob_dict[nuc],10)+prob
		prob = prob1
	return prob	
	

def binom_prob(num, prob):
	comp_prob = 1- (10**prob)
		
	result = 1- comp_prob**num
										 
	return ("%.3f" % result)
	
with open('rosalind_rstr.txt', 'r') as f:   
	seq_list = []
	seq = ''
	for lin in f:
		seq_list.append(lin.strip())

	seq = seq_list[1]
	GC_list = []
	num = ''
	for x in seq_list[0]:
		if x != ' ':
			num += x
		elif x == ' ':
			GC_list.append(int(num))	
			num = ''
	GC_list.append(float(num))
		
print GC_list
print seq

print binom_prob(GC_list[0],log_prob(seq,GC_list[1]))			