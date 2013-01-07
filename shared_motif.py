import sys
import collections
import re
seq_list = []
patt = []
match =[]
matchl =[]
done = []
final_motif_list =[]
def split_len(seq):
	split = []
	fin_split =[]
	slen = [seq[start:end] for start in range(len(seq)-1) for end in range(2,len(seq)+1)]
	for s in slen:
		if s != '' and len(s)>15 and len(s)<251:
			split.append(s)
	return list(set(split))	
	
            	
ln = 1
cnt = 0
patte = []
match_arr = []
with open("rosalind_lcs.txt", "r") as f:
	for lin in f:
		seq_list.append(lin.strip())
	patt = split_len(seq_list[0])  	
	for other in range(len(seq_list)):
		print other
		if other < 2:
			pattern = patt
		else:
			patter = sorted(match_arr[other-1], key = len)
			pattern = patter[-20:]
		for p in pattern:
			if seq_list[0] != seq_list[other]:
				if p in seq_list[other]:
					match.append(p)
					match_list = collections.Counter(match)
		match_arr.append(set(match))		
						
	print len(match_arr)							
	for c in match_list.items():
		if c[1] == len(seq_list)-1:
			final_motif_list.append(c[0])
			final_motif_list.sort(key = len)
			final_motif_list.reverse()	
	print final_motif_list[0]
