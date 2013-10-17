import numpy as np
import sys



def find_ls(n, seq):
	s1 = np.zeros(shape =(n,1))
	s2 = np.zeros(shape =(n,1))
	for i in range(n):
		x = 0
		for i2 in range(n):
			if seq[i] < seq[i2]:
				s1[i] += 1
			if seq[i] > seq[i2]:
				s2[i] += 1

	inc_list = []
	dec_list = []			
	for pos, num in enumerate(s1):
		if pos < len(s1)-1:	
			if num > max(s1[int(pos+1):]):
				inc_list.append(seq[pos])	
		else:
			if seq[pos] > inc_list[-1:]:
				inc_list.append(seq[pos])
	for pos2, num2 in enumerate(s2):
		if pos2 < len(s2)-1:	
			if num2 > max(s2[int(pos2+1):]):
				dec_list.append(seq[pos2])	
		else:
			if seq[pos2] < dec_list[-1:]:
				dec_list.append(seq[pos2])
												
	for ni in range(len(inc_list)):
		sys.stdout.write(str(inc_list[ni])+' ')
		if ni == len(inc_list)-1:
			sys.stdout.write('\n')
	for nd in range(len(dec_list)):
		sys.stdout.write(str(dec_list[nd])+' ')
		if nd == len(dec_list)-1:
			sys.stdout.write('\n')		
				
		


with open('rosalind_lgis.txt', 'r') as f:   
	seq_list = []
	seq = ''
	seq_part = ''
	for lin in f:
		for s in lin:
			if s.isdigit():
				seq_part +=s
			elif s == ' ' or s =='\n':
				seq_list.append(int(seq_part))
				seq_part = ''	

	n = seq_list[0]
	nums = seq_list[1:]
	find_ls(n, nums)	
			

