def StRut():
	# n = 5
	# eastCoords = {0:(0, 4), 1:(2, 3), 2:(4, 2), 3:(6, 6)}
	# northCoords = {4:(7, 1)}

	n = int(input())
	eastCoords = {}
	northCoords = {}
	for line in range(n):
		temp = input().split()
		if temp[0] == 'E':
			eastCoords[line] = (int(temp[1]), int(temp[2]))
			# eastCoords.append([int(temp[1]), int(temp[2]), line])
		elif temp[0] == 'N':
			northCoords[line] = (int(temp[1]), int(temp[2]))
			# northCoords.append([int(temp[1]), int(temp[2]), line])

	# get the collisions in the form [(east id, north id, x difference, y difference)]
	# only possible collisions indluded
	collisions = []		
	for ei in eastCoords:
		ex, ey = eastCoords[ei]
		for ni in northCoords:
			nx, ny = northCoords[ni]
			if nx > ex and ey > ny:
				collisions.append((ei, ni, nx-ex, ey-ny))
	timeSortC = sorted(collisions, key = lambda x:max(x[2], x[3]))
	del(collisions)

	# stopped is {cow id: (x or y where cow gets stopped, id that stopped them)}
	# records who stops who
	blame = [0 for i in range(n)]
	stopped = {}
	for collide in timeSortC:
		ei, ni, xdiff, ydiff = collide
		# print(stopped)
		if ei not in stopped and xdiff > ydiff:
			if ni not in stopped or stopped[ni][0] > eastCoords[ei][1]:
				#print(ni+1, "stops", ei+1)
				stopped[ei] = (northCoords[ni][0], ni)
				blame[ni] += blame[ei]+1
				if ni in stopped:
					blame[stopped[ni][1]] += 1

		elif ni not in stopped and ydiff > xdiff:
			if ei not in stopped or stopped[ei][0] > northCoords[ni][0]:
				#print(ei+1, "stops", ni+1)
				stopped[ni] = (eastCoords[ei][1], ei)
				blame[ei] += blame[ni]+1
				if ei in stopped:
					blame[stopped[ei][1]] += 1
		# print(blame)
		# print(stopped)

	for item in blame:
		print(item)

if __name__ == '__main__':
	StRut()