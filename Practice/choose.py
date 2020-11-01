def main():
	n = 5
	r = 3
	memo = {}
	ans = fact(n,memo) / fact(r,memo) / fact(n-r,memo)
	print(ans)


def fact(n,memo):
	if n in memo:
		return memo[n]
	if n == 0 :
		memo[n] = 1
		return 1
	memo[n] = fact(n-1,memo) * n
	return memo[n]

if __name__ == '__main__':
	main()