def main():
	with open('cereal.in') as file:
		lines = file.read().splitlines()
		n = int(lines[0].split(" ")[0])
		m = int(lines[0].split(" ")[0])
		available = [None for _ in range(m)]
		first = []
		second = []
		ans = []

		for i in range(0,n):
			ans.append(0)
		print("available", available)
		for i in range(0,n):
			print(i)
			first.append(int(lines[i+1].split(" ")[0]))
			second.append(int(lines[i+1].split(" ")[1]))
		for i in range(0,n):
			for j in range(0,m):
				available[j] = True;
			for j in range(0, n-i):
				if available[first[i+j]]:
					available[first[i+j]] = False
					ans[i] += 1
				elif available[second[i+j]]:
					available[second[i+j]] = False
					ans[i] += 1
	with open('cereal.out', 'w') as file:
		for item in ans:
			file.write(str(item) + "\n")










if __name__ == '__main__':
	main()