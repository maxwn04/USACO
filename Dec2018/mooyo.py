def mooyo ():
	with open('mooyomooyo.in') as file:
		lines = file.read().splitlines()
		grid = []
		n = int(lines[0].split()[0])
		k = int(lines[0].split()[1])
		for row in range(0,n):
			grid.append([])
			for column in range(0,10):
				grid[row].append(int(lines[row+1][column]))
		been = {}
		done = False
		times = 0
		while not done:
			times += 1
			done = True
			been = {}
			for r, row in enumerate(grid):
				for c, space in enumerate(row):
					if not space == 0 and not (r,c) in been:
						componentList = component(n, (r, c), grid, been)
						if len(componentList) >= k:
							#print("big component")
							done = False
							for spot in componentList:
								been[spot] = 1
			for spot in been:
				if been[spot] == 1:
					r, c = spot
					grid[r][c] = 0
			newgrid = falling(n, grid)
			grid = newgrid

		#print (newgrid)
	with open('mooyomooyo.out', 'w') as file:
		for row in grid:
			for space in row:
				file.write(str(space))
			file.write('\n')
		#print(been)

					


def component(n, coords, graph, been):
	points = []
	points.append(coords)
	row, column = coords
	been[coords] = 0
	color = graph[row][column]
	if row+1 < n and not (row+1, column) in been and graph[row+1][column] == color:
		points += component(n, (row+1, column), graph, been)		
	if row-1 >= 0 and not (row-1, column) in been and graph[row-1][column] == color:
		points += component(n, (row-1, column), graph, been)
	if column+1 < 10 and not (row, column+1) in been and graph[row][column+1] == color:
		points += component(n, (row, column+1), graph, been)
	if column-1 >= 0 and not (row, column-1) in been and graph[row][column-1] == color:
		points += component(n, (row, column-1), graph, been)
	return points


def falling(n, graph):
	done = False
	while not done:
		done = True
		for row in range(n-1):
			for column in range(10):
				if row+1 < n and graph[row][column] > 0 and graph[row+1][column] == 0:
					graph[row+1][column] = graph[row][column]
					graph[row][column] = 0
					done = False
							
	return graph

if __name__ == '__main__':
	mooyo()