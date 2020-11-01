def main():
	string1 = "sunday"
	string2 = "saturday"
	i = len(string1) - 1
	j = len(string2) - 1

	memo = [[None for a in range(j+1)]for b in range(i+1)]
	print(lcs(i, j, string1, string2, memo, 0))	
	print (str(sorted(memo)))


def lcs(i, j, s1, s2, memo, pmatch):
	if i == j and i == 0:
		if s1[i]==s2[j]:
			memo[i][j] = 0
			return memo[i][j]
		memo[i][j] = 1
		return memo[i][j]
	match = 1
	if s1[i] == s2[j] :
		match = 0

	#print(i,j, memo)
	memo[i][j] = min([lcs(i-1, j, s1, s2, memo, match) if i-1 >= 0 else i+1, 
		lcs(i, j-1, s1, s2, memo, match) if j-1 >= 0 else j+1, 
		lcs(i-1, j-1, s1, s2, memo, match) if i-1 >= 0 and j-1 >= 0 else i+j+2]) + match
	return memo[i][j]

if __name__ == '__main__':
	main()