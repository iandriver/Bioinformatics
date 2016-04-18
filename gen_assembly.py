
    
    
def find_overlap(start, arr, beg, ck_list):
	
	r = len(start)
	if beg == 1:
		l = int((len(start)/2)+40)
	else:
		l = (len(arr[0])/2)+40
	x = range(1, l)
	for i in reversed(x):
		first_part = start[-i:]
		for ind, seq in enumerate(arr):
			full = len(seq)
			h = int((len(seq)/2)-1)
			for j in range(h,full+1):
				'''print first_part, 'k', seq[0:j]'''
				if first_part == seq[0:j] and ind not in ck_list:
					print first_part, 'new', seq[j:full]
					ck_list.append(ind)
					print ck_list
					return [ck_list, start+seq[j:full]]
def find_start(arr):
	for index, a in enumerate(arr):
		total = 0
		for ar in arr:	
			if a[0:int(len(a)/2)-10] in ar:
				total+=1
		if total ==1 :
			print index
			return index		
			
def merge_string(arr):
	count = 0
	overlap = []
	start = find_start(arr)
	check_list = [start]
	final = find_overlap(arr[start], arr, 1, check_list)
	old_final= final[1]
	ncheck_list = final[0]
	for le in range(0, len(arr)+1):
		print le
		final = find_overlap(old_final, arr, 0, ncheck_list)
		if final != None:
			old_final = final[1]
			ncheck_list = final[0]
			count+=1
			print 'count', count				
	return old_final						
with open('rosalind_long.txt', 'r') as f:   
	seq_list = []
	for lin in f:
		seq_list.append(lin.strip())
	print len(seq_list)
	print merge_string(seq_list) 