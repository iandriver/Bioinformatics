import itertools
import sys
from sets import Set

def sign_perm(elements):
	all_list = []
	all_list.append(elements)

	for perm in all_perms(elements[1:]):
		short_list = []
		for i in range(len(elements)):
			short_list.append([-y for y in perm[:i]] + elements[0:1] + perm[i:])
			short_list.append(perm[:i] + [-y for y in elements[0:1]] + perm[i:])
			short_list.append(perm[:i] + elements[0:1] + [-y for y in perm[i:]])
			short_list.append([-y for y in perm[:i]] + [-y for y in elements[0:1]] + [-y for y in perm[i:]])
			short_list.append([-y for y in perm[:i]] + elements[0:1] + [-y for y in perm[i:]])
			short_list.append([-y for y in perm[:i]] + [-y for y in elements[0:1]] + perm[i:])
			short_list.append(perm[:i] + [-y for y in elements[0:1]] + [-y for y in perm[i:]])
			for s in short_list:
				if s not in all_list:
					all_list.append(s)
				
	return all_list		
		

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
				#nb elements[0:1] works in both string and list contexts
				yield perm[:i] + elements[0:1] + perm[i:]
c= 0
k = []	
for z in all_perms([1,2,3]):
	k.append(sign_perm(z))
	c+=1
	print c

all_perm = [item for sublist in k for item in sublist if isinstance(item, list)]
all_perm.sort()
final = list(all_perm for all_perm,_ in itertools.groupby(all_perm))
print len(final)

for a in final:
	old = str(a).strip('[]')
	new = old.replace(',', '')
	sys.stdout.write(new+'\n')