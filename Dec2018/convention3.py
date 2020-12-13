import math

def convention():
    with open ('convention.in') as file:
        lines = file.read().splitlines()
        split = lines[0].split()
        n = int(split[0])
        m = int(split[1])
        c = math.ceil(n/m)
        split = lines[1].split()
        arrivalTimes = []
        for i in range(n):
            arrivalTimes.append(int(split[i]))

        arrivalTimes = sorted(arrivalTimes)
        cow_i = 0
        for bus in range(m):
            minCows = max(1, len(arrivalTimes) - cow_i - c*(busesLeft-1))
            maxCows = min(c, len(arrivalTimes) - cow_i)
            for i in range(minCows, maxCows+1):
                time = max(bus(cow_i+i, arrivalTimes, busesLeft-1, c), 
                arrivalTimes[cow_i+i-1] - arrivalTimes[cow_i])
        #print(time)
        busWaitTime.append(time)
    with open('convention.out', 'w') as file:        
        file.write(str(maxwait))

if __name__ == '__main__':
    convention()