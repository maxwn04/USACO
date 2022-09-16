def paintbarn():
    with open ('paintbarn.in') as file:
        lines = file.read().splitlines()
        n = int(lines[0].split()[0])
        k = int(lines[0].split()[1])
        coords = [[], [], [], []]
        edges = {}
        for i in range(n):
            line = lines[1+i].split()
            coords[0].append(int(line[0]))
            coords[1].append(int(line[1]))
            coords[2].append(int(line[2]))
            coords[3].append(int(line[3]))
        for i in range(n):
            frontx = coords[0][i]
            backx = coords[2][i]
            if not frontx in edges:
                edges[frontx] = []
            if not backx in edges:
                edges[backx] = []
            edges[frontx].append((coords[1][i], coords[3][i], 1))
            edges[backx].append((coords[1][i], coords[3][i], -1))
        print(edges)
        counter = 0
        ans = 0
        prevx = 0
        keysorted = sorted(edges)

        for y in range(1000):
            for x in keysorted:
                if counter == k:
                    ans += x - prev
                for item in edges[x]:
                    a,b,c = item
                    if a <= y and y < b:
                        counter += c
                prev = x
                
        print(ans)
    with open('paintbarn.out', 'w') as file:        
        file.write(str(ans))

if __name__ == '__main__':
    paintbarn()
