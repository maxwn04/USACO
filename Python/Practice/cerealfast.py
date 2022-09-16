def main():
	with open('cereal.in') as file:
		lines = file.read().splitlines()
		cows = int(lines[0].split(" ")[0])
		cereals = int(lines[0].split(" ")[0])
		takenfirst = {}
		takensecond = {}
		ans = [0 for _ in range(cows)]
		for i in range(1,cereals+1):
			takenfirst[i] = 0
			takensecond[i] = 0;
		for i in range(cows):
			takenfirst[int(lines[i+1].split(" ")[0])] +=1
			takensecond[int(lines[i+1].split(" ")[1])] +=1
		for i in range(cows):
			for j in range(cereals):
				if int(taken[j+1]) > 0 :
					ans[i] += 1
			taken[int(lines[i+1].split(" ")[0])] -=1
			taken[int(lines[i+1].split(" ")[1])] -=1
	with open('cereal.out', 'w') as file:
		for item in ans:
			file.write(str(item) + "\n")






if __name__ == '__main__':
	main()