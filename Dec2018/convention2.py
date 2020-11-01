def convention():
    with open ('convention.in') as file:
        lines = file.read().splitlines()
        split = lines[0].split()
        n = int(split[0])
        m = int(split[1])
        c = int(split[2])
        split = lines[1].split()
        arrivalTimes = []
        for i in range(n):
            arrivalTimes.append(int(split[i]))

        arrivalTimes = sorted(arrivalTimes)
        #print(arrivalTimes)
        ans = bus(0, arrivalTimes, m, c)
        #print(ans)
    with open('convention.out', 'w') as file:        
        file.write(str(ans))

def bus(cow_i, arrivalTimes, busesLeft, c):
    if cow_i == len(arrivalTimes):
        return 0
    if busesLeft == 0:
        return float('inf')
    busWaitTime = []
    minCows = max(1, len(arrivalTimes) - cow_i - c*(busesLeft-1))
    maxCows = min(c, len(arrivalTimes) - cow_i)
    #print(cow_i, minCows, maxCows)
    for i in range(minCows, maxCows+1):
        time = max(bus(cow_i+i, arrivalTimes, busesLeft-1, c), 
            arrivalTimes[cow_i+i-1] - arrivalTimes[cow_i])
        #print(time)
        busWaitTime.append(time)
    #print(cow_i, busesLeft, busWaitTime)
    return min(busWaitTime)

if __name__ == '__main__':
    convention()