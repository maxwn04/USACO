import math
manurePiles = []

def teleportation():
    with open ('teleport.in') as file:
        global manurePiles
        lines = file.read().splitlines()
        split = lines[0].split()
        n = int(split[0]) 
        for i in range(n):
            split = lines[1+i].split()
            a, b = (int(split[0]), int(split[1]))
            manurePiles.append((a, b))
        del(split)
        del(lines)

        #ranges is in the form {position: [cow id range bot], [cow id range top]]}
        #setting up ranges
        ranges = {}
        ranges[0] = [[], []]
        for i in range(n):
            a, b = manurePiles[i]
            if not (abs(a) > abs(a-b)) and not (abs(a) > abs(b)):
                if (a > 0 and b > 0) or (a < 0 and b < 0):
                    ranges.setdefault(2*a, [[], []])
                    ranges.setdefault(2*b-2*a, [[], []])
                    ranges[min(2*a, 2*b-2*a)][0].append(i)
                    ranges[max(2*a, 2*b-2*a)][1].append(i)
                elif (a < 0 and b > 0) or (a > 0 and b < 0):
                    ranges.setdefault(2*b, [[], []])
                    ranges[min(0, 2*b)][0].append(i)
                    ranges[max(0, 2*b)][1].append(i)

        # finding the maximum intersection
        # returns the indices of the cows using said intersection
        order = sorted(ranges)
        curLen = 0
        maxLen = 0
        curUsingTp = []
        cowsUsingTp = []
        for i in range(len(order)):
            space = order[i]
            for item in ranges[space][0]:
                curUsingTp.append(item)
                curLen += 1
            for item in ranges[space][1]:
                curUsingTp.remove(item)
                curLen -= 1
            if curLen > maxLen:
                maxLen = curLen
                cowsUsingTp = curUsingTp.copy()
        del(curUsingTp)

        # Ends of the cows using tp
        cowEndsUsingTp = sorted(list(map(lambda x:manurePiles[x][1], cowsUsingTp)))
        del(cowsUsingTp)
        y = math.floor(maxLen/2)


        ans = dist(cowEndsUsingTp[y])
        print(ans)

    with open('teleport.out', 'w') as file:        
        file.write(str(ans))

# returns the total distance for a certain tp endpoint
def dist(y):
    ans = 0
    for item in manurePiles:
        a, b = item
        ans += min(abs(a-b), abs(a)+abs(b-y))
    return ans



if __name__ == '__main__':
    teleportation()