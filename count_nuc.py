def count_nuc(str):
	ac = 0
	cc = 0
	gc = 0
	tc = 0
	for n in str:
		if n == 'A':
			ac +=1
		if n =='C':
			cc += 1
		if n == 'G':
			gc += 1
		if n == 'T':
			tc += 1	
	print ac, cc, gc, tc				

with open('rosalind_ini.txt', 'r') as f:   
	seq_list = []
	seq = ''
	for lin in f:
		seq_list = lin.strip()
		
count_nuc(seq_list)		