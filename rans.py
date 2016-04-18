from math import log
import sys

def log_prob(seq, GC_prob):
	prob_dict ={'A':(1-GC_prob)/2, 'T':(1-GC_prob)/2, 'C':GC_prob/2, 'G':GC_prob/2}
	prob = log(prob_dict[seq[0]], 10)
	for nuc in seq[1:]:
		prob1 = log(prob_dict[nuc],10)+prob
		prob = prob1
	return prob	







with open('rosalind_prob.txt', 'r') as f:   
	seq_list = []
	seq = ''
	for lin in f:
		seq_list.append(lin.strip())
	print seq_list
	seq = seq_list[0]
	GC_list = []
	num = ''
	for x in seq_list[1]:
		if x != ' ':
			num += x
		elif x == ' ':
			GC_list.append(float(num))
			num = ''
		
	GC_list.append(float(num))
	print seq
	print GC_list	
	
	for GC in GC_list:
		z = log_prob(seq, GC)
		sys.stdout.write(str("%.3f" % z)+' ')
	sys.stdout.write('\n')				