import itertools
import numpy as np

def hamming1(str1, str2):
  return sum(itertools.imap(str.__ne__, str1, str2))
  
def dist_array(seq_list):
	dist_ar = np.zeros(shape=(len(seq_list), len(seq_list)), dtype = "float")
	np.set_printoptions(precision= 5)
	for i1, a1 in enumerate(seq_list):
		for i2, a2 in enumerate(seq_list):
			if hamming1(a1, a2) != 0:
				b= float(hamming1(a1, a2))
				c= b/float(len(a1))
				dist_ar[i1][i2] = c
			else:
				dist_ar[i1][i2] = 0.0	
			b= float(hamming1(a1, a2))
			c= b/float(len(a1))
			print b,c 
	print dist_ar		
  
with open('rosalind_pdst.txt', 'r') as f:   
	seq_list = []
	seq = ''
	for lin in f:
		if lin[0] != '>':
			seq += lin.strip()
		else:
			if seq != '':
				seq_list.append(seq)
				seq = ''
	if seq != '':
		seq_list.append(seq)
		
print seq_list
dist_array(seq_list)		