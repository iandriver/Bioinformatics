def tree_count(n):
	for z in range(2, 15):
		if n<4:
			nearest = 2
		elif n>= 2**z:
			nearest = z
	s= 0
	dif = n-(2**nearest)
	print dif, 'd'
	print nearest, 'n'
	for x in range(1, nearest):
		s+=2**x
		print s
	print s
	print s- dif
			

		
tree_count(3485)