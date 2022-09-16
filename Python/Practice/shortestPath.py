def main():
	n = 0
	aMap = {0: [(1, 1), (2, 2), (3, 28)], 
	1: [(4, 4), (5, 2)], 
	2: [(4, 9), (5, 5), (6, 16)], 
	3: [(6, 2)], 4: [(7, 18)], 
	5: [(7, 13)], 6: [(7, 2)]}
	end = 7
	a = actualPath(n,end,aMap)
	
	print(a)

def actualPath(n,end,aMap):
	memo = {}
	pDict = {}
	shortestPath(n,end,aMap,pDict,memo)
	path = ""
	at = end
	while(True):
		if at == n:
			break
		at = pDict[at]
		path += " >-- {}".format(at)
	path = path[::-1]
	path += str(end)
	return path

def shortestPath(n, end, aMap, pDict, memo):
	if n in memo:
		return memo[n]
	if n == end:
		memo[n] = 0
		return memo[n]
	small = float('inf')

	for pair in aMap[n]:
		node, length = pair
		a = length + shortestPath(node,end,aMap,pDict,memo)
		pDict[node] = n
		if a < small:
			small = a

	memo[n] = small
	return(small)


if __name__ == '__main__':
	main()