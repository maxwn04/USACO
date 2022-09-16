def buckets():
	with open('test/' + '1'+'.in') as file:
		lines = file.read().splitlines()
		grid = []
		startRow = 0
		startColumn = 0
		for row in range(0,10):
			grid.append([])
			for column in range(0,10):
				grid[row].append(lines[row][column])
				if lines[row][column] == 'L':
					startRow = row
					startColumn = column
		print(shortPath(startRow, startColumn, grid))
		#print(grid)

def shortPath(barnRow, barnColumn, grid):
	been = {(barnRow, barnColumn):True}
	queue = [(barnRow, barnColumn, 0)]
	while(True):
		#print(queue)
		row, column, cows = queue.pop(0)
		if grid[row][column] == 'B':
			return cows -1
		if row + 1 < 10 and not (row+1, column) in been and not grid[row+1][column] == 'R':
			been[(row+1, column)] = True
			queue.append((row+1, column, cows+1))
		if row - 1 >= 0 and not (row-1, column) in been and not grid[row-1][column] == 'R':
			been[(row-1, column)] = True
			queue.append((row-1, column, cows+1))
		if column + 1 < 10 and not (row, column+1) in been and not grid[row][column+1] == 'R':
			been[(row, column+1)] = True
			queue.append((row, column+1, cows+1))
		if column-1 >= 0 and not (row, column-1) in been and not grid[row][column-1] == 'R':
			been[(row, column-1)] = True
			queue.append((row, column-1, cows+1))



if __name__ == '__main__':
	buckets()