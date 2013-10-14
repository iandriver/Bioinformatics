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
				if maxn > 10:
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
    start = find_start(words)
    result = words[start]
    match_list = [start]
    for index, word in enumerate(words):
    	if index not in match_list:
			mx, nx = glue(result, word)
			my, ny = glue(word, result)
			if mx:
				result = nx
				match_list.append(index)
			elif my:
				result = ny	
				match_list.append(index)
	while len(match_list)<len(words):
		for index, word in enumerate(words):
			if index not in match_list:
				mx, nx = glue(result, word)
				my, ny = glue(word, result)
				if mx:
					result = nx
					match_list.append(index)
				elif my:
					result = ny	
					match_list.append(index)				
    return result
    
				
		
				
with open('rosalind_long.txt', 'r') as f:   
	seq_list = []
	seq = ''
	for lin in f:
		if lin[0] != '>':
			seq += lin.strip()
		else:
			seq_list.append(seq)
			seq = ''
	seq_list.append(seq)
	print merge_string(seq_list) 
