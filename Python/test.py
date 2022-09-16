def main():
	lines = ['1', '5', '3']
	a = [1, 2, 4, 5, 9]
	b = [3, 7, 3, 4, 5]

	path = list(map(lambda x: int(x), lines))
	print(a+b)
	print(path)

def hi(n):
	print(n+a+b)

if __name__ == '__main__':
	main()