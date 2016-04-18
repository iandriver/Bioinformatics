from sets import Set
import numpy as np

def longest_common_substring(src, dst) :
	c = np.zeros((len(src), len(dst)), dtype=np.int)
	z = 0
	src_m = None
	dst_m = None
	for i in range(len(src)) :
		for j in range(len(dst)) :
			if src[i] == dst[j] :
				if i == 0 or j == 0 :
					c[i,j] = 1
				else :
					c[i, j] = c[i-1, j-1] + 1
				if c[i, j] > z :
					z = c[i, j]
				if c[i, j] == z :
					src_m = (i-z+1, i+1)
					dst_m = (j-z+1, j+1)
			else :
				c[i, j] = 0
	return src_m, dst_m

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
	debru = []
	fin = []
	for z in tot_list:
		debru.append([z[:-1], z[1:]])
	for y in debru:
		for x in debru:
			if y[1] == x[0]:
				fin.append(y[0]+x[1][-2:])
	print fin
	fin1 = []
	for x in range(0, len(fin)):
		for d in range(0, len(fin)):
			if x != d:
				lcs1, lcs2 = longest_common_substring(fin[x], fin[d])
				if len(fin[x][lcs1[0]:lcs1[1]]) >3 and (lcs1[1]+1) == len(fin[x]):
					fin1.append(fin[x]+fin[d][lcs2[1]])
	print fin1




def glue(a, b):
    maxn = 0
    match = False
    if b in a:
    	match = True
    	return match, a
    else:
		for n in xrange(1, 1 + min(len(a), len(b))):
			suffix = a[-n:]
			prefix = b[:n]
			if prefix == suffix and n > maxn:
				maxn = n
				match = False
				if maxn > len(a)-2:
					match = True
		return match, a + b[maxn:]

def find_start(arr):
	for index, a in enumerate(arr):
		total = 0
		for ar in arr:
			if a[0:int(len(a)/2)] in ar:
				total+=1
		if total == 1 :
			return index

def merge_string(words):
    if not words: return ""
    result = words[0]
    result_list = []
    match_list = [0]
    for index, word in enumerate(words):
		if index not in match_list:
			mx, nx = glue(result, word)
			my, ny = glue(word, result)
			if mx:
				result_list.append(nx)
				match_list.append(index)
			elif my:
				result_list.append(ny)
				match_list.append(index)
    return result_list



with open('/Users/idriver/Documents/rosalind_input/rosalind_debru.txt', 'r') as f:   
	seq_list = []
	seq = ''
	for lin in f:
		seq_list.append(lin.strip())

print seq_list
a = debruijn(seq_list)
print a
