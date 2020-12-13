def main():
	s = [2,5,7]
	n = 100
	s = sorted(s)
	print(coin(n,s,0))

def coin(n,s,i):
	counter = 0
	if n == 0:
		return 1
	if n < 0:
		return 0
	for j in range(i,len(s)):
		counter += coin(n-s[j], s, j)
	return counter

if __name__ == '__main__':
	main()