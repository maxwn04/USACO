def main():
	memo = {}
	ans = eggDrop(2,36,memo)
	print(ans)
	print(memo)

def eggDrop(n,k,memo):
	
	if (n,k) in memo:
		return memo[(n,k)]

	if k == 1:
		memo[(n,k)] = 1
		return 1

	if n == 0:
		memo[(n,k)] = 0
		return float("inf")

	if n == 1:
		memo[(n,k)] = k
		return k

	small = k
	for i in range(1,k+1):

		x = max(eggDrop(n-1,i-1,memo), eggDrop(n,k-i-1,memo))
		#print(n,k,x)
		if x < small:
			small = x

	memo[(n,k)] = small+1
	return memo[(n,k)]

if __name__ == '__main__':
	main()