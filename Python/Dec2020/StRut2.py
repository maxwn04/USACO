def StRut():
	# n = 5
	# eastCoords = {0:(0, 4), 1:(2, 3), 2:(4, 2), 3:(6, 6)}
	# northCoords = {4:(7, 1)}

	n = int(input())
	eastCoords = []
	northCoords = []
	for line in range(n):
		temp = input().split()
		if temp[0] == 'E':
			eastCoords.append([int(temp[1]), int(temp[2]), line])
		elif temp[0] == 'N':
			northCoords.append([int(temp[1]), int(temp[2]), line])

	eastOrder = sorted(eastCoords, key = lambda x: x[1])
	northOrder = sorted(northCoords, key = lambda x: x[0])

	stopped = {}
	blame = [0 for i in range(n)]

	for eCow in eastOrder:
		ex, ey, ei = eCow
		for nCow in northOrder:
			nx, ny, ni = nCow
			if nx > ex and ey > ny and not ni in stopped and not ei in stopped:
				if nx-ex > ey-ny:
					stopped[ei] = 1
					blame[ni] += 1 + blame[ei]
				if nx-ex < ey-ny:
					stopped[ni] = 1
					blame[ei] += 1 + blame[ni]
	for item in blame:
		print(item)

if __name__ == '__main__':
	StRut()