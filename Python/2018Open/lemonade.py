def lemonade():
    with open ('test.in') as file:
    	lines = file.read().splitlines()
    	split = lines[0].split()
    	n = int(split[0])
    	split =lines[1].split()
    	w = []
    	for i, item in enumerate(split):
    		w.append(int(item))
    	w = sorted(w)
    	w = w[::-1]
    	lineSize = 0
    	for i in range(n):
    		if w[i] < lineSize:
    			break
    		lineSize += 1
    	print(lineSize)
    with open('test.out', 'w') as file:        
        file.write(str(lineSize))


if __name__ == '__main__':
	lemonade()