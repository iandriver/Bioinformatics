import sys
from collections import Counter


def s_beau(st):
	scnt = Counter()
	for sen in st:
		for let in sen:
			scnt[let.lower()] +=1
	rank_let = scnt.most_common()
	val = 26
	tot = 0
	for p in rank_let:
		tot += val * p[1]
		val -= 1
	print tot	
			


seq = []
with open(str(sys.argv[1]), "r") as f:
    #iterate over each line in file
    for l in f:
    	temp_set = []
    	r= ''
    	for wor in l:
    		if wor.isalpha():
    			r+=wor

    	if r != '' and r.isalpha():		
    		temp_set.append(str(r))		
    	seq.append(temp_set)
for s in seq:
	s_beau(s)   	    	