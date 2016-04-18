from sets import Set
import sys

with open('rosalind_seto.txt', 'r') as f: 
	fin_set_list = []
	for lin in f:
		l= lin.strip()
		if l[0] != '{':
			n = int(l)
			set_list = []
		else:
			num = ''
			for x in l:
				if x.isdigit():
					num += x
				if x == ',':
					set_list.append(int(num))
					num = ''
				if x == '}':
					set_list.append(int(num))
					fin_set_list.append(set_list)
					set_list = []
	set1 = Set(fin_set_list[0])
	set2 = Set(fin_set_list[1])
	ans =[]
	ans.append(list(set1.union(set2)))
	ans.append(list(set1.intersection(set2)))
	ans.append(list(set1.difference(set2)))
	ans.append(list(set2.difference(set1)))
	ans.append(list(Set(range(1,n+1)).difference(set1)))
	ans.append(list(Set(range(1,n+1)).difference(set2)))
	
	for a in ans:
		sys.stdout.write('{')
		z = range(len(a))
		for pos in z:
			if pos != z[-1]:
				sys.stdout.write(str(a[pos])+', ')
			else:
				sys.stdout.write(str(a[pos])+'}'+'\n')	
		
			
	
						