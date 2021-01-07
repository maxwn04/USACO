import math

def restStops():
    with open ('reststops.in') as file:
        lines = file.read().splitlines()
        split = lines[0].split()
        length = int(split[0])
        numStops = int(split[1])
        johnSpeed = int(split[2])
        bessieSpeed = int(split[3])
        speedDiff = johnSpeed - bessieSpeed
        restStops = []
        for i in range(numStops):
            split = lines[i+1].split()
            restStops.append((int(split[0]), int(split[1])))
        tastysort = sorted(restStops, key = lambda x:-x[1])
        tastyScore = 0
        on = 0
        for i, item in enumerate(tastysort):
            if item[0] > on:
                tastyScore += (item[0]-on)*(speedDiff)*item[1]
                on = item[0]
    with open('reststops.out', 'w') as file:        
        file.write(str(tastyScore))

if __name__ == '__main__':
    restStops()