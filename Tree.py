import collections
import numpy as np
from sets import Set
import itertools

def create_node(ar1, ar2):
	return list(Set(ar1+ar2))


def node_count(nodes, branches):
	all_nodes = range(1, nodes+1)
	nodes_pres = [item for sublist in branches for item in sublist]
	nodes_missing = [a for a in all_nodes if a not in [b for b in nodes_pres]]
	return nodes_missing


def node_merge(branche):
	o_node_list = branche
	node_list = []
	for nod in branche:	
		node_list.append(nod)
	print node_list, 'nl1111'
	del_list = []
	for p, i in enumerate(branche):
		for p2, i2 in enumerate(branche):
			if Set(i) != Set(i2) and p != p2 and p not in del_list and p2 not in del_list:
				b= None
				g= np.array(i)
				h= np.array(i2)
				if len(i) >= len(i2):
					val = any(np.in1d(g, h))
				else:
					val = any(np.in1d(h,g))
				if val:		
					b = create_node(i, i2)
				print val, i, i2, b
				if b != None:
					a= True
					for x in node_list:
						if Set(b) == Set(x):
							a = False
							print b, x, a
						
					if not a:
						if len(node_list[p]) <= len(node_list[p2]):
							del_list.append(p)
						else:
							del_list.append(p2)	
					else:
						node_list.append(b)
						del_list.append(p)
						del_list.append(p2)				
						
	del_list.sort()
	dele_list = list(Set(del_list))
	print dele_list, 'dl'
	new_node_list = []
	if dele_list == []:
		results = o_node_list
	else:	
		for i, x in enumerate(node_list):
			if i not in dele_list:
				new_node_list.append(x)
		print new_node_list, 'nnl'			
		results = node_merge(new_node_list)
		
	return results	
		


with open('rosalind_tree.txt', 'r') as f:   
	sets = []
	for ln in f:
		sets.append(ln.strip())
	nodes = int(sets[0])
	del sets[0]
	branches = []	
	for y in sets:
		branches.append([int(s) for s in y.split() if s.isdigit()])
			
	print branches
			
	nodes_results = node_merge(branches)
	nodes_m = node_count(nodes, branches)
	for x in nodes_m:
		nodes_results.append([x])
	print nodes_results
	print len(nodes_results)-1	
	
