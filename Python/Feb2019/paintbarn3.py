def paintbarn():
    with open ('test/1.in') as file:
        lines = file.read().splitlines()
        n = int(lines[0].split()[0])
        k = int(lines[0].split()[1])
        coords = [[], [], [], []]
        startbox = {}
        endbox = {}
        for i in range(n):
            line = lines[1+i].split()
            coords[0].append(int(line[0]))
            coords[1].append(int(line[1]))
            coords[2].append(int(line[2]))
            coords[3].append(int(line[3]))
        for i in range(n):
            frontx = coords[0][i]
            backx = coords[2][i]
            if not frontx in startbox:
                startbox[frontx] = []
            if not backx in endbox:
                endbox[backx] = []
            startbox[frontx].append((coords[1][i], coords[3][i]))
            endbox[backx].append((coords[1][i], coords[3][i]))
        counter = 0
        ans = 0
        for y in range(1000):
            for x in range(1000):
                if x in startbox:
                    for item in startbox[x]:
                        a,b = item
                        if a <= y and y < b:
                            counter += 1
                if x in endbox:
                    for item in endbox[x]:
                        a,b = item
                        if a <= y and y < b:
                            counter -= 1
                if counter == k:
                    ans += 1
        print(ans)
    with open('paintbarn.out', 'w') as file:        
        file.write(str(ans))

if __name__ == '__main__':
    paintbarn()
