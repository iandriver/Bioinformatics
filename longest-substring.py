import sys
from collections import Counter
import numpy

'''lcs takes two strings of any length and returns the longest common subsequence (non-consecutive or consecutive)
as long as the order is the same in the two sequences'''
def lcs(string1, string2):
  dim1 = max(len(string1), len(string2))
	match_array = numpy.tile(0, (len(string1), len(string2)))
	score_array = numpy.tile(0, (len(string1), len(string2)))
	for num1, let1 in enumerate(string1):
		for num2, let2 in enumerate(string2):
			if let1 == let2:
				match_array[num1, num2] = 1		

	for r, x in enumerate(match_array):
		for c, lt in enumerate(x):
			if lt == 1 and  c == len(string2)-1:
				score_array[r,c] = 1
			elif c < len(string2)-1:
				if lt == 1 and match_array[r,c+1] == 0:	
					score_array[r,c] = numpy.sum(match_array[r+1:len(string1),c+1:len(string2)])+match_array[r,c]			
	i, j =numpy.unravel_index(score_array.argmax(), score_array.shape)
	ans = ''
	start = string1[i]
	ans+=start								
	for py, sy in enumerate(score_array):
		for px, sx in enumerate(sy):
			if py == i+1 and px == j+1:
				find_max=score_array[py:len(string1), px:len(string2)]
				i1, j1 =numpy.unravel_index(find_max.argmax(), find_max.shape)
				if find_max[i1,j1] != 0:
					i2= i1+i+1
					j2= j1+j+1
					ans+=string1[i2]
					i=i2
					j= j2	
	return ans		

#list of sequences
seq = []
with open(str(sys.argv[1]), "r") as f:
	#iterate over each line in file
	for l_num, l in enumerate(f):
		#create variable to mark semicolon break position in each line
		col_num = 0
		#find strings in each line unless line is blank
		if l[0] != ' ' and l[0] != '\n':
			for pos, let in enumerate(l):
				#find colon and save sub array of two strings on either side
				if let == ';':
					seq.append([l[0:pos], l[pos+1:].strip()])

	for i in range(len(seq)):
		print lcs(seq[i][0], seq[i][1])


