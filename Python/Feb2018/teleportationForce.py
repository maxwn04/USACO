import math
manurePiles = []

def teleportation():
    with open ('test.in') as file:
        global manurePiles
        lines = file.read().splitlines()
        split = lines[0].split()
        n = int(split[0]) 
        for i in range(n):
            split = lines[1+i].split()
            a, b = (int(split[0]), int(split[1]))
            manurePiles.append((a, b))

        ans = float('inf')
        cur = 0
        for i in range (-15, 16):
        	cur = dist(i)
        	if ans > cur:
        		ans = cur

        print(ans)


def dist(y):
    ans = 0
    for item in manurePiles:
        a, b = item
        ans += min(abs(a-b), abs(a)+abs(b-y))
    return ans


if __name__ == '__main__':
	teleportation()
