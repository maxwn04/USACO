def rectPasture():
	n = input()
	coords = {}
	for line in range(n):
		coords.append(input().split()+{line})
	ysorted = sorted(coords, key = lambda x:x[1]);
	y = ""
	for i in range(n):
		y += ysorted[i][2];
		y += "-"
	del(ysorted)

	ans = n*(n-1)

	compare = ""
	xsorted = sorted(coords, key = lambda x:x[0])
	for i in range(n):
		for j in range(i+1, n):
			xsorted

	

