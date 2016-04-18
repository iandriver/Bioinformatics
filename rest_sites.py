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
	
with open('rosalind_eval.txt', 'r') as f:   
	seq_list = []
	seq = ''
	for lin in f:
		seq_list.append(lin.strip())

	seq = str(seq_list[1])
	len_seq = int(seq_list[0])
	GC_list = []
	num = ''
	for x in seq_list[2]:
		if x != ' ':
			num += x
		elif x == ' ':
			GC_list.append(float(num))	
			num = ''
	GC_list.append(float(num))


print len_seq		
print GC_list
print seq
for gc_prob in GC_list:
	if gc_prob == 0.0 or gc_prob == 1.0:
		print '0'
	else:
		prob = 10**log_prob(seq, gc_prob)
		result = prob*(len_seq-1)
		print "%.3f" % result
	
			
			
		