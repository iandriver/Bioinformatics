from math import factorial as fac
from itertools import permutations as pt
from sets import Set

def pair_check(pair, pair_list, cat_list):
	nums = abs(pair[0]-pair[1])
	check_list = []
	cat_pair = []
	curr_index = pair_list.index(pair)
	if nums == 1 and pair[0] not in cat_list and pair[1] not in cat_list:
		check_list.append(pair[0])
		check_list.append(pair[1])
		a = Set(cat_list).union(Set(check_list))
		if curr_index < len(pair_list)-1:
			pair_check(pair_list[curr_index+1], pair_list, a)
		else:
			return a	
	elif (nums-1) % 2 == 0:	
		for p in pair_list:
			if p[0] not in cat_list and p[1] not in cat_list:
				if max(p)< max(pair) and min(p) > min(pair) and p[0] not in check_list and p[1] not in check_list:
					check_list.append(p[0])
					check_list.append(p[1])
		clist = Set(check_list)
		if clist == Set(range(pair[0]+1, pair[1])):
			print clist		
			a = Set(cat_list).union(Set(check_list))
			if curr_index < len(pair_list)-1:
				pair_check(pair_list[curr_index+1], pair_list, a)			
			else:
				return a
		else:
			if curr_index < len(pair_list)-1:
				pair_check(pair_list[curr_index+1], pair_list, cat_list)
			else:
				return cat_list								
	else:
		if curr_index < len(pair_list)-1:
			pair_check(pair_list[curr_index+1], pair_list, cat_list)
		else:
			return cat_list			
			

def catlan(num_pairs, pair_list):
	c =0
	tot_pairs = []
	for p in pair_list:
		plist = pair_check(p, pair_list, [])
		print plist
		if plist != None:
			if len(plist) == num_pairs*2:
				c+=1
	print c				

def per_match(seq):
	a_count = 0
	u_count = 0
	g_count = 0
	c_count = 0
	a_index = []
	u_index = []
	c_index = []
	g_index = []
	for i, nuc in enumerate(seq):
		if nuc == 'A':
			a_count += 1
			a_index.append(i)
		if nuc == 'G':
			g_count += 1
			g_index.append(i)
		if nuc == 'U':
			u_count += 1
			u_index.append(i)
		if nuc == 'C':
			c_count += 1
			c_index.append(i)
	au_list = []
	gc_list = []
	for a in a_index:
		for u in u_index:
			if (min(a,u), max(a,u)) not in au_list:
				au_list.append((min(a,u), max(a,u)))
	for c in c_index:
		for g in g_index:
			if (min(c,g), max(c,g)) not in gc_list:
				gc_list.append((min(c,g), max(c,g)))
	pair_list = list(Set(au_list+gc_list))							
	pair_list.sort()
	print pair_list
	catlan((a_count+g_count), pair_list)
	

		

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
print seq_list[0]		
per_match(seq_list[0])
		