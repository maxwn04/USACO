n = 0
b = 0
path = []
boots = []
memo = {}
def snowBoots():
    with open ('snowboots.in') as file:
        global n, b, path, boots, memo
        lines = file.read().splitlines()
        split = lines[0].split()
        n = int(split[0])
        b = int(split[1])
        split = lines[1].split()
        path = list(map(lambda x:int(x), split))
        for i in range(b):
            split = lines[2+i].split()
            boots.append((int(split[0]), int(split[1])))
        ans = step(0, 0)
        #print(memo)
        #print(ans)

        
    with open('snowboots.out', 'w') as file:        
        file.write(str(ans))


def step(space, boot):
    global n, b, path, boots, memo
    if (space, boot) in memo:
        return memo[(space, boot)]
    if space == n-1:
        memo[(space, boot)] = boot
        return boot
    if boot == b-1:
        memo[(space, boot)] = boot
        return boot
    options = []
    #moves = []
    options.append(step(space, boot+1))
    #moves.append((space, boot+1))
    depth, length = boots[boot]
    if depth >= path[space]:
        for i in range(space+1, min(n, space+length+1)):
            if path[i] <= depth:
                options.append(step(i, boot))
                #moves.append((i, boot))
    #print(space, boot, moves)
    ans = min(options)
    memo[(space, boot)] = ans
    return ans


if __name__ == '__main__':
    snowBoots()