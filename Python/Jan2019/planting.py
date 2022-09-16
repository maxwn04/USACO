def planting():
    with open ('planting.in') as file:
    	lines = file.read().splitlines()
    	n = int(lines[0])
    	alist = {}
    	for i in range(n):
    		alist[i+1] = []
    	for i in range(n-1):
    		a = int(lines[i+1].split()[0])
    		b = int(lines[i+1].split()[1])
    		alist[a].append(b)
    		alist[b].append(a)
    	maxlen = 0
    	for i in range(n):
    		if len(alist[i+1]) > maxlen:
    			maxlen = len(alist[i+1])
    	ans = maxlen+1
    	print(ans)
    with open('planting.out', 'w') as file:        
        file.write(str(ans))


if __name__ == '__main__':
   	planting()   

