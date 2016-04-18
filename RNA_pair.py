from math import factorial as fac

def per_match(seq):
	au_count = 0
	gc_count = 0
	for nuc in seq:
		if nuc == 'A':
			au_count += 1
		if nuc == 'G':
			gc_count += 1
	result = fac(au_count)*fac(gc_count)
	print result

with open('rosalind_pmch.txt', 'r') as f:   
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

seq_list
seq1= seq_list[0]
print seq1
per_match(seq1)