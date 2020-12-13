import sys

def perimeter():
    with open ('test/1.in') as file:
        print(sys.getrecursionlimit())
        exit()
        lines = file.read().splitlines()
        n = int(lines[0])
        grid = lines[1:]
        #print(grid)
        been = {}
        largest = 0
        perimeter = 0

        for x in range(n):
            for y in range(n):
                if (x, y) not in been:
                    been[(x, y)] = 1
                    if grid[x][y] == '#':
                        blobSize, blobPerimeter = sizeperimeter(n, grid, x, y, been)

                        if blobSize > largest:
                            largest = blobSize
                            perimeter = blobPerimeter
                        elif blobSize == largest:
                            perimeter = min(perimeter, blobPerimeter)
        print(largest, perimeter)
    # with open('perimeter.out', 'w') as file:        
    #     file.write(str(largest))
    #     file.write(' ')
    #     file.write(str(perimeter))



def sizeperimeter(n, grid, x, y, been):
    been[(x, y)] = 1
    perimeter = 4
    area = 1
    if x+1 < n and (x+1, y) not in been and grid[x+1][y] == '#':
        a,p = sizeperimeter(n, grid, x+1, y, been)
        area += a
        perimeter += p
    if y+1 < n and (x, y+1) not in been and grid[x][y+1] == '#':
        a,p = sizeperimeter(n, grid, x, y+1, been)
        area += a
        perimeter += p
    if x-1 >= 0 and (x-1, y) not in been and grid[x-1][y] == '#':
        a,p = sizeperimeter(n, grid, x-1, y, been)
        area += a
        perimeter += p
    if y-1 >= 0 and (x, y-1) not in been and grid[x][y-1] == '#':
        a,p = sizeperimeter(n, grid, x, y-1, been)
        area += a
        perimeter += p
    if x+1 < n and grid[x+1][y] == '#':
        #print('here1')
        perimeter -= 1
    if y+1 < n and grid[x][y+1] == '#':
        #print('here2')
        perimeter -= 1
    if x-1 >= 0 and grid[x-1][y] == '#':
        #print('here3')
        perimeter -= 1
    if y-1 >= 0 and grid[x][y-1] == '#':
        #print('here4')
        perimeter -= 1
    #print(x, y, perimeter)
    return (area, perimeter)

if __name__ == '__main__':
    perimeter()
