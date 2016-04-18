import sys

def match_dna(dna, mis_allowed, match):
	match_list = []
	for i in range(len(dna)):
		match_count = 0
		if len(match) == len(dna[i:i+len(match)]):
			curr_dna = dna[i:i+len(match)]
			for pos, let in enumerate(curr_dna):
				if let != match[pos]:
					match_count += 1
				if match_count > mis_allowed:
					break
			if match_count <= mis_allowed:
				match_list.append([match_count, curr_dna])
	match_list.sort(key=lambda tup: tup[1])
	match_list.sort(key=lambda tup: tup[0])
	if match_list == []:
		print 'No match'
	else:
		ans = [x[1] for x in match_list]
		ans1 = str(ans).strip('[]')
		ans2 = ans1.strip(' ').replace('\'', '')
		print ans2.replace(',', '')		
					
					
				
			
			



test_cases = open(sys.argv[1], 'r')
for test in test_cases:
	test = test.rstrip()
	if(0 == len(test)):
		continue
	parts = test.split(" ")
	match = parts[0]
	mis_allowed = int(parts[1])
	dna = parts[2]
	match_dna(dna, mis_allowed, match)

	