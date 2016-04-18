from sets import Set
from itertools import permutations
import numpy as np
import re
import sys
nuc = 'ACGT'

nuc_lex = []
all_perm = []
nuc_lex2 = []
for c in range(4):
	for c2 in range(4):
		nuc_lex.append(nuc[c]*3+nuc[c2]*1)
		nuc_lex.append(nuc[c]*2+nuc[c2]*2)
		nuc_lex.append(nuc[c]*1+nuc[c2]*3)
	for n in nuc_lex:
		all_perm.append([''.join(p) for p in permutations(n)])
all_perm2 = [item for sublist in all_perm for item in sublist]		
nuc_perm = [''.join(p) for p in permutations(nuc)]	

all_lex = list(Set(nuc_lex+nuc_perm+all_perm2))
for a in all_lex:
	for a2 in all_lex:
		nuc_lex2.append(a[0:2]+a2[2:4])
all_lex2 = list(Set(nuc_lex2+all_lex))		
all_lex2.sort()
print all_lex2



def kmer(seq_list, all_lex):
	mercount = np.zeros(len(all_lex))
	for i, a in enumerate(all_lex):
		mercount[i] = len([m.start() for m in re.finditer('(?='+str(a)+')', str(seq_list))])
	for ni in range(len(mercount)):
		sys.stdout.write(str(int(mercount[ni]))+' ')
		if ni == len(mercount)-1:
			sys.stdout.write('\n')

with open('rosalind_kmer.txt', 'r') as f:   
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
	
	kmer(seq_list, all_lex2)	

