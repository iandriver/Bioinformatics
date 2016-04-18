import sys

def overlap(a, b):
	# takes two strings a and b and a threshold for minimum overlap
    maxn = 0
    #if b is in a just return a
    if b in a:
    	return len(a), a
    else:	
		for n in xrange(1, 1 + min(len(a), len(b))):
			#iterate through a from the end and b from the begining
			suffix = a[-n:]
			prefix = b[:n]
			#if prefix matches suffix and it is longer than previous maxn (or 0) store new max
			if prefix == suffix and n > maxn:
				maxn = n
		#return True and new string if match was found			    
		return maxn, a + b[maxn:]
    
def find_start(arr):
	# given an list of strings arr find the longest starting string 
	mis_index =[] #index of strings found in other strings, so can't be the start
	match_index = [] #potential starting strings
	for ind_pos, a in enumerate(arr):
		for ar in arr:
			if a[0:int(len(ar)/2)] in ar:
				# if the first part of string a is in string ar add it to start matches
				match_index.append(ind_pos)
				if ar.index(a[0:int(len(ar)/2)]) != 0:
					# if that string is anywhere other than index 0 add it to the mis index
					mis_index.append(ind_pos)
	longest = 0
	for st in [x for x in match_index if x not in mis_index]:
		#take the indexes of all the strings found at index 0 only and take the longest one
		if len(arr[st]) >= longest:
			longest = len(arr[st])
			sta = st										
	return sta	#return the starting index 			
			
def merge_string(words):
	if not words:
		return ""
	else:	
		while len(words) > 1:
			best_overlap = 1
			repl_i1 = None
			repl_i2 = None
			best_glu = None
			for i1, w1 in enumerate(words):
				for i2, w2 in enumerate(words):
					if i1!= i2:
						max_overlap, glued = overlap(w1, w2)
						if max_overlap > best_overlap:
							best_overlap= max_overlap
							repl_i1 = i1
							repl_i2 = i2
							best_glu = glued					
			del words[max(repl_i1, repl_i2)]
			del words[min(repl_i2, repl_i1)]
			words.append(best_glu)
		return words		
    				
    				
    				
 
    
seq = []
with open(str(sys.argv[1]), "r") as f:
    #iterate over each line in file
    for l in f:
    	temp_set = []
    	r= ''
    	for wor in l:
    		if wor != ';':
    			r+=wor
    		else:
    			temp_set.append(r)
    			r= ''
    	temp_set.append(r.strip())		
    	seq.append(temp_set)		
    	    	
for x in seq:
	z = merge_string(x)
	if z[0] != '':
		print z[0]