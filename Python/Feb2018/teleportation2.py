import math
manurePiles = []

def teleportation():
    with open ('teleport.in') as file:
        global manurePiles
        lines = file.read().splitlines()
        split = lines[0].split()
        n = int(split[0]) 
        criticalValues = {}
        length = 0
        for i in range(n):
            split = lines[1+i].split()
            a, b = (int(split[0]), int(split[1]))
            manurePiles.append((a, b))
            length += abs(a-b)
        del(split)
        del(lines)

        criticalValues[0] = 0
        for i in range(n):
            a, b = manurePiles[i]
            if not (abs(a) > abs(a-b)) and not ((a > b and b > 0) or (a < b and b < 0)):
                if (a > 0 and b > 0) or (a < 0 and b < 0):
                    criticalValues.setdefault(2*a, 0)
                    criticalValues.setdefault(2*b-2*a, 0)
                    criticalValues.setdefault(b, 0)
                    criticalValues[2*a] -= 1
                    criticalValues[2*b-2*a] -= 1
                    criticalValues[b] += 2
                elif (a < 0 and b > 0) or (a > 0 and b < 0):
                    criticalValues.setdefault(2*b, 0)
                    criticalValues.setdefault(b, 0)                    
                    criticalValues[b] += 2
                    criticalValues[0] -= 1
                    criticalValues[2*b] -= 1

        order = sorted(criticalValues)
        curSpace = order[0]
        ans = length
        slope = 0
        for item in order:
            length += slope*(item-curSpace)
            if length < ans:
                ans = length
            slope += criticalValues[item]
            curSpace = item

        # Plug and Chug all Cv's
        # for item in criticalValues:
        #     cur = dist(item)
        #     if ans > cur:
        #         ans = cur


        # print(ans)

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