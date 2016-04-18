# the number is ugly if it is divisible by 2, 3, 5 or 7.
# given a string of digits, count how many expressions with plus and minus interleaved
# are evaluated to ugly number.

# C[i,p] = number of numbers which is p modulo 210(2*3*5*7) for str[:i].
#        = sum { C[j,(p + z * str[j:i] mod 210)] for every possible j and z in (-1,1) }
# (of course C[1,p] = (str[0] == p then 1 else 0))
# uglynum = sum { C[len(str),p] for every possible p divisible by 2, 3, 5 or 7 }

def process(digits):
    table = [[], [int(int(digits[0]) == k) for k in xrange(210)]]
    #print [(x, table[-1][x]) for x in xrange(210) if table[-1][x] != 0]
    for i in xrange(2, len(digits) + 1):
        row = []
        for j in xrange(210):
            num = int(int(digits[:i]) % 210 == j)
            for k in xrange(1, i):
                rhs = int(digits[k:i])
                num += table[k][(j + rhs) % 210]
                num += table[k][(j - rhs) % 210]
            row.append(num)
        table.append(row)
        #print [(x, table[-1][x]) for x in xrange(210) if table[-1][x] != 0]
    return sum(table[-1][k] for k in xrange(210) if k%2==0 or k%3==0 or k%5==0 or k%7==0)

import sys

seq= []    
with open(str(sys.argv[1]), "r") as f:
    #iterate over each line in file
    for l in f:
    	temp_set = []
    	r= ''
    	for num in l:
    		if num.isdigit():
    			r+=num
    		else:
    			temp_set.append(r)
    			r= ''
    	if r != '':		
    		temp_set.append(r)
    	if temp_set[0] != '':			
    		seq.append(temp_set[0])
    		
for i in seq:
	numuglys = process(i)
	print numuglys



