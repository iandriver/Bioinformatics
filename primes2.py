import sys

def primes2(n):
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]

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
    			temp_set.append(int(r))
    			r= ''
    	if r != '':		
    		temp_set.append(int(r))		
    	seq.append(temp_set[0])
dict_done = {}
for x in seq:
	p = primes2(x)  
	new = str(p).strip('[]')
	print new.replace(' ', '')	 