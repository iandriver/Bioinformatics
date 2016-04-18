import sys


def fb(fb_set):
	a= fb_set[0]
	b= fb_set[1]
	c= fb_set[2]
	ans =[]
	for x in range(1,c+1):
		if x%(a*b)==0:
			ans.append('FB')
		elif x%a == 0:
			ans.append('F')
		elif x%b == 0:
			ans.append('B')
		else:
			ans.append(str(x))	
	for i, y in enumerate(ans):
		if i <len(ans)-1:
			sys.stdout.write(y+' ')	
		else:
			sys.stdout.write(y+'\n')					
		
	


seq = []
with open(str(sys.argv[1]), "r") as f:
    #iterate over each line in file
    for l in f:
    	temp_set = []
    	r= ''
    	for num in l:
    		if num.isdigit():
    			r+=num
    			print r
    		else:
    			temp_set.append(int(r))
    			r= ''
    	if r != '':		
    		temp_set.append(int(r))		
    	seq.append(temp_set)
    for x in seq:
    	fb(x)			
    				
    	
	