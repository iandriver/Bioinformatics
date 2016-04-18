from math import factorial as fac

def per_match(seq):
	a_count = 0
	u_count = 0
	g_count = 0
	c_count = 0
	for nuc in seq:
		if nuc == 'A':
			a_count += 1
		if nuc == 'G':
			g_count += 1
		if nuc == 'U':
			u_count += 1
		if nuc == 'C':
			c_count += 1
	if a_count == u_count:
		au_pair = fac(a_count)
	else:
		au_pair = fac(max(a_count, u_count))/fac(max(a_count, u_count)-min(a_count, u_count))
	if g_count == c_count:
		gc_pair = fac(g_count)
	else:
		gc_pair = fac(max(g_count, c_count))/fac(max(g_count, c_count)-min(g_count, c_count))

	result = (au_pair*gc_pair)
	print result

with open('rosalind_mmch.txt', 'r') as f:   
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