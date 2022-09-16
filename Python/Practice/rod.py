def main():
	p = {1:1, 2:5, 3:8, 4:9, 5:10, 6:17, 7:17, 8:20}
	memo = {0:0}
	print(price(p,memo,8))

def price(p,memo,l):
	print(l)
	if l in memo:
		return memo[l]
	max = 0
	for i,cost in p.items():
		if not l-i < 0:
			num = price(p,memo,l-i) + cost
		if num > max:
			max = num
	memo[l] = max
	return max

if __name__ == '__main__':
	main()