from sets import Set

revcomp_dict= {"A" : "T", "C" : "G", "T":"A", "G":"C"}

def debruijn(seq_list):
	n_seq_list= []
	for seq in seq_list:
		comp = ''
		for nuc in reversed(seq):
			comp += revcomp_dict[nuc]
		n_seq_list.append(comp)
	tot_list = list(Set(n_seq_list+seq_list))
	tot_list.sort()
	
	for z in tot_list:
		print '('+str(z[:-1])+', '+str(z[1:])+')'

with open('rosalind_debru.txt', 'r') as f:   
	seq_list = []
	seq = ''
	for lin in f:
		seq_list.append(lin.strip())
		
print seq_list
debruijn(seq_list)		