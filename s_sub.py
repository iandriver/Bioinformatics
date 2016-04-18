import sys

def check_pos(i, check_list,len):
	ans = False
	for x in range(i,i+len):
		if x not in check_list:
			ans = True
		else:
			return False
	if ans:
		return ans		
				
	
def s_sub(to_sub, subs):
	check_list = []
	for s_pos in range(0, len(subs),2):
		curr_len = len(subs[s_pos])
		to_find = subs[s_pos]
		to_add = subs[s_pos+1]
		sub_diff = len(to_add) - len(to_find)
		for i in range(len(to_sub)):
			if to_sub[i:i+curr_len] == to_find and check_pos(i, check_list, curr_len):
				to_sub = to_sub[0:i] + to_add + to_sub[i+curr_len:]
				for c in range(len(check_list)):
					if check_list[c]> i+curr_len:
						new_c = check_list[c] + sub_diff
						check_list[c] = new_c	
				for x in range(i, i+curr_len):
					check_list.append(x)
				break	
	print to_sub				
					
				
				
			
		

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	test = test.rstrip()
	if(0 == len(test)):
		continue
	parts = test.split(";")
	to_sub1 = parts[0]
	sub_parts = parts[1].split(',')
	s_sub(to_sub1, sub_parts)
	