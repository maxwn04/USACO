def perimeter():
    with open ('perimeter.in') as file:
        lines = file.read().splitlines()
        n = int(lines[0])
        grid = lines[1:]
        #print(grid)
        been = [[0 for _ in range(n)] for __ in range(n)]
        largest = 0
        perimeter = 0
        largeBlob = []
        for x in range(n):
            for y in range(n):
                if been[x][y] == 0:
                    been[x][y] = 1
                    if grid[x][y] == '#':
                        queue = [(x,y)]
                        blobSize = findSize(n, grid, been, queue)

                        if blobSize > largest:
                            largest = blobSize
                            largeBlob = []
                            largeBlob.append((x, y))
                        elif blobSize == largest:
                            largeBlob.append((x, y))
        perimeter = float('inf')
        for i in range(len(largeBlob)):
            blobPerimeter = findPerimeter(n, grid, been, [(largeBlob[0][1], largeBlob[0][1])])
            if  blobPerimeter < perimeter:
                perimeter = blobPerimeter
        print(largest, perimeter)

    with open('perimeter.out', 'w') as file:        
        file.write(str(largest))
        file.write(' ')
        file.write(str(perimeter))



def findSize(n, grid, been, queue): 
    area = 0
    while(len(queue) > 0):
        area += 1
        x, y = queue.pop()
        if x+1 < n and grid[x+1][y] == '#':
            
            if been[x+1][y] == 0:
                been[x+1][y] = 1
                queue.append((x+1, y))
        if x-1 >= 0 and grid[x-1][y] == '#':
            
            if been[x-1][y] == 0:
                been[x-1][y] = 1
                queue.append((x-1, y))
        if y+1 < n and grid[x][y+1] == '#':
            
            if been[x][y+1] == 0:
                been[x][y+1] = 1
                queue.append((x, y+1))
        if y-1 >= 0 and grid[x][y-1] == '#':
            
            if been[x][y-1] == 0:
                been[x][y-1] = 1
                queue.append((x, y-1))
        #print(x, y, area, perimeter)
    return area

def findPerimeter(n, grid, been, queue): 
    perimeter = 0
    while(len(queue) > 0):
        perimeter += 4
        x, y = queue.pop()
        if x+1 < n and grid[x+1][y] == '#':
            perimeter -= 1
            if been[x+1][y] == 1:
                been[x+1][y] += 1
                queue.append((x+1, y))
        if x-1 >= 0 and grid[x-1][y] == '#':
            perimeter -= 1
            if been[x-1][y] == 1:
                been[x-1][y] += 1
                queue.append((x-1, y))
        if y+1 < n and grid[x][y+1] == '#':
            perimeter -= 1
            if been[x][y+1] == 1:
                been[x][y+1] += 1
                queue.append((x, y+1))
        if y-1 >= 0 and grid[x][y-1] == '#':
            perimeter -= 1
            if been[x][y-1] == 1:
                been[x][y-1] += 1
                queue.append((x, y-1))
        #print(x, y, area, perimeter)
    return perimeter


if __name__ == '__main__':
    perimeter()
