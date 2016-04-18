import sys
from collections import defaultdict
from sets import Set

def getsubs(loc, s):
	substr = s[loc:]
	i = -1
	while(substr):
		yield substr
		substr = s[loc:i]
		i -= 1

def longestRepetitiveSubstring(r, minocc):
	string_num = ''
	for num in r:
		string_num += str(num)+' '
	occ = defaultdict(int)
	# tally all occurrences of all substrings
	for i in range(len(string_num)):
		for sub in getsubs(i,string_num):
			occ[sub] += 1

	# filter out all substrings with fewer than minocc occurrences
	occ_minocc = [k for k,v in occ.items() if v >= minocc]

	if occ_minocc:
		maxkey =  max(occ_minocc, key=len)
		i_maxkey = []
		l = ''
		for lett in maxkey:
			if lett != ' ':
				l+= lett
			elif l.isdigit():
				i_maxkey.append(int(l))
				l =''
		if len(i_maxkey) == 4 and i_maxkey[:2] == i_maxkey[2:]:
			red_max = i_maxkey[:2]
		elif len(i_maxkey)%2 == 0:		
			for pos in range(2, len(i_maxkey)-2):
				if i_maxkey[:2] == i_maxkey[pos:pos+2]:
					red_max = i_maxkey[:pos]
		elif len(list(Set(i_maxkey))) == 1:
			count_seq = defaultdict(int)
			for c in r:
				count_seq[int(c)] += 1
			result = max(count_seq.iteritems(), key = lambda x: x[1])
			r1 = str(result[0])+' '
			r2 = r1 *  int(result[1]/2)	
			return r2.strip()	
		else:
			red_max = i_maxkey				
		ans = ''
		for rm in red_max:
			ans += str(rm)
			ans += ' '
		ans1= ans.strip()
		return ans1
		
	else:
		raise ValueError("no repetitions of any substring of '%s' with %d or more occurrences" % (r,minocc))
            
seq = []
with open(str(sys.argv[1]), "r") as f:
	#iterate over each line in file
	for l in f:
		temp_set = []
		r= ''
		for wor in l:
			if wor.isdigit():
				r+=wor
			elif wor == ' ':	
				temp_set.append(r)
				r= ''
			elif wor == '\n' and temp_set != []:
				temp_set.append(r)	
				seq.append(temp_set)
	if temp_set != []:
		seq.append(temp_set)  
		
for s in seq:
	print longestRepetitiveSubstring(s, 2)
			          