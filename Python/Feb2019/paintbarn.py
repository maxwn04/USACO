def paintbarn():
    with open ('paintbarn.in') as file:
        lines = file.read().splitlines()
        n = int(lines[0].split()[0])
        k = int(lines[0].split()[1])
        coords = [[], [], [], []]
        for i in range(n):
            line = lines[1+i].split()
            coords[0].append(int(line[0]))
            coords[1].append(int(line[1]))
            coords[2].append(int(line[2]))
            coords[3].append(int(line[3]))
        minX = min(coords[0])
        minY = min(coords[1])
        maxX = max(coords[2])
        maxY = max(coords[3])
        score = {}
        ans = 0
        for x in range(minX, maxX):
            for y in range(minY, maxY):
                score[(x,y)] = 0
                for r in range(n):                  
                    if x >= coords[0][r] and x < coords[2][r] and y >= coords[1][r] and y < coords[3][r]:
                        score[(x,y)] += 1
                if score[(x, y)] == k:
                    ans += 1
        print(ans)
    with open('paintbarn.out', 'w') as file:        
        file.write(str(ans))


if __name__ == '__main__':
    paintbarn()