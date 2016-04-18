import itertools
n = int(input())
print(2**n)
for i in range(0,n+1):
    a = list(itertools.combinations([x+1 for x in range(n)], i))
    for j in a:
        print("{", ", " .join(map(str,j)), "}", sep="")

def powerset(seq):
    """
    Returns all the subsets of this set. This is a generator.
    """
    if len(seq) <= 1:
        yield seq
        yield []
    else:
        for item in powerset(seq[1:]):
            yield [seq[0]]+item
            yield item
        
a=powerset(range(1, 825))
c= 0
for x in a:
	print x
	c+=1
print c	
	  
        