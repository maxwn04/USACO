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

        score = {}
        ans = 0
        for r in range(n):
            for x in range(coords[0][r], coords[2][r]):
                for y in range(coords[1][r], coords[3][r]):
                    if (x, y) not in score:
                        score[(x, y)] = 0 
                    score[(x, y)] += 1
        for item in score:
            if score[item] == k:
                ans += 1
        print(ans)
    with open('paintbarn.out', 'w') as file:        
        file.write(str(ans))


if __name__ == '__main__':
    paintbarn()