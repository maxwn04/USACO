import math

def convention():
    with open ('test/1.in') as file:
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
        maxwait = 0
        first = 0
        counter = 0
        for i in range(n):
            if counter == 0:
                first = arrivalTimes[i]
            counter += 1
            if counter == c:
                counter = 0
                wait = arrivalTimes[i]-first
                if wait > maxwait:
                    maxwait = wait
    # with open('convention.out', 'w') as file:        
    #     file.write(str(maxwait))

if __name__ == '__main__':
    convention()