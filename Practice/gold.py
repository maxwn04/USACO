def main():
	m = 4
	n = 4
	mat = [[1, 3, 1, 5], 
    	   [2, 2, 4, 1], 
           [5, 0, 2, 3], 
           [0, 6, 1, 2]] 
	memo = {}
	starts = []
	for i in range (m):
		starts.append(gold(i,0,memo,mat))

	print (max(starts), sorted(memo.items()))


def gold(r,c, memo, mat):
	if (r,c) in memo:
		#print(r,c)
		return memo[r,c]
	m = len(mat)
	n = len(mat[0])
	if c == n-1:
		memo[r,c] = mat[r][c]
		return memo[r,c]
	# if c == 0:
	# 	print (max(gold(r,c+1,memo,mat), gold(min(r+1,m-1) ,c+1,memo,mat))

	memo[r,c] = mat[r][c] + max([gold(r,c+1,memo,mat), gold(min(r+1,m-1) ,c+1,memo,mat), 
	    gold(max(r-1,0),c+1,memo,mat)])
	return memo[r,c]

if __name__ == '__main__':
	main()