def mountains():
    with open ('mountains.in') as file:
        lines = file.read().splitlines()
        n = int(lines[0])
        peaks = {}
        
        for i in range(n):
            xPeak = int(lines[i+1][0])
            yPeak = int(lines[i+1][2])
            if int(xPeak) in peaks:
                if yPeak > peaks[xPeak]:
                    peaks[xPeak] = yPeak
            else:
                peaks[xPeak] = yPeak
        
        order = sorted(peaks)
        y = -order[0]+peaks[order[0]]
        up = True
        numPeakNext = 0
        nextPeakCoord = (order[0], peaks[order[0]])
        ans = 0
        for x in range(max(order)):
            if x == nextPeakCoord[0]:
                if peaks[x] == y:
                    up = False
                    ans += 1

                numPeakNext += 1
                nextPeakCoord = (order[numPeakNext], peaks[order[numPeakNext]])

            if y <= (x-nextPeakCoord[0]) + nextPeakCoord[1]:
                up = True
                y = (x-nextPeakCoord[0]) + nextPeakCoord[1]

            if up == True:
                y += 1
            else:
                y -= 1
        #print(ans)



    with open('mountains.out', 'w') as file:        
        file.write(str(ans))


if __name__ == '__main__':
    mountains()