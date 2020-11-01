def mountains():
    with open ('mountains.in') as file:
        lines = file.read().splitlines()
        n = int(lines[0])
        startEnd = {}
        for i in range(n):
            x = int(lines[i+1][0])
            y = int(lines[i+1][2])
            if y-x in startEnd and y+x > peaks[y-x]:
                    startEnd[y-x] = y+x
            else:
                startEnd[y-x] = y+x
        
        order = sorted(startEnd)
        #print(order)
        endPoint = 0
        peaks = 0
        for peak in order:
            if startEnd[peak] >= endPoint:
                endPoint = startEnd[peak]
                peaks += 1
        #print(peaks)
    with open('mountains.out', 'w') as file:        
        file.write(str(peaks))

if __name__ == '__main__':
    mountains()