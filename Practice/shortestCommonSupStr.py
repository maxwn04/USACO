def main():
	string1 = "adkjghb"
	string2 = "xdofijb"
	i = len(string1) - 1
	j = len(string2) - 1

	memo = [[None for a in range(j+1)]for b in range(i+1)]
	print(i+j+2 - lcs(i, j, string1, string2, memo, 0))	
	print (str(sorted(memo)))


def lcs(i, j, s1, s2, memo, pmatch):
	if i == j and i == 0:
		if s1[i]==s2[j]:
			memo[i][j] = 1
			return memo[i][j]
		memo[i][j] = 0
		return memo[i][j]
	match = 0
	if s1[i] == s2[j] and pmatch == 0:
		match = 1

	#print(i,j, memo)
	memo[i][j] = max([lcs(i-1, j, s1, s2, memo, match) if i-1 >= 0 else 0, lcs(i, j-1, s1, s2, memo, match) if j-1 >= 0 else 0]) + match
	return memo[i][j]

if __name__ == '__main__':
	main()