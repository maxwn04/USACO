

nums = [2,7,11,17]
for i in range(len(nums)):
	for j in range(i,len(nums)):
		if i+j == target:
			return [i,j]