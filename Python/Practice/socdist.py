def main():
	with open('socdist.in') as file:
		lines = file.read().splitlines()
		n = int(lines[0].split(" ")[0])
		m = int(lines[0].split(" ")[1])
		lower = []
		upper = []
		for i in (0,n):
			lower.append(lines[i].split(" ")[0])
			upper.append(lines[i+1].split(" ")[1])
		upper.sort()
		lower.sort()
		ans = Math.floor((upper[-1]+1-lower[0])/m)
	with open('socdist.out', 'w') as file:
		file.write(str(ans))


if __name__ == '__main__':
	main()