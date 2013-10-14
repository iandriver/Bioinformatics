import itertools

def hamming1(str1, str2):
  return sum(itertools.imap(str.__ne__, str1, str2))
  
def rev_comp(str):
	rev_dict = {'A':'T', 'C':'G', 'T':'A', 'G':'C'}
	nums = range(0, len(str))
	rev_str= ''
	for rn in nums[::-1]:
		rev_str += rev_dict[str[rn]]	
	return rev_str
	
def find_match(str_list):
	match_list = []
	incorr_dict = { x: y for x,y in enumerate(str_list)}
	for i, mstr in enumerate(str_list):
		for i2, mstr2 in enumerate(str_list):
			if i != i2:
				if mstr == mstr2 or mstr == rev_comp(mstr2):
					if [i, i2] not in match_list and [i2, i] not in match_list:
						match_list.append([i, i2])
						try:
							del incorr_dict[i]
							del incorr_dict[i2]
						except KeyError:
							pass
						
		
	return match_list, incorr_dict
	
def near_match(match_list, incorr_dict, str_list):
	trans_list =[]
	for pair in match_list:
		for k, v in incorr_dict.items():
			if 	hamming1(str_list[pair[0]], v) == 1:
				if [v, str_list[pair[0]]] not in trans_list:
					trans_list.append([v, str_list[pair[0]]])
			if 	hamming1(str_list[pair[1]], v) == 1:
				if [v, str_list[pair[1]]] not in trans_list:
					trans_list.append([v, str_list[pair[1]]])
			if 	hamming1(rev_comp(str_list[pair[0]]), v) == 1:
				if [v, rev_comp(str_list[pair[0]])] not in trans_list:
					trans_list.append([v, rev_comp(str_list[pair[0]])])
			if 	hamming1(rev_comp(str_list[pair[1]]), v) == 1:
				if [v, rev_comp(str_list[pair[1]])] not in trans_list:
					trans_list.append([v, rev_comp(str_list[pair[0]])])
	for p in trans_list:
		print p[0]+'->'+p[1]			
			  
with open('rosalind_corr.txt', 'r') as f:   
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
	
	m, i = find_match(seq_list)
	near_match(m, i, seq_list)
