def mountains():
    with open ('test/1.in') as file:
        lines = file.read().splitlines()
        n = int(lines[0])
        peaks = []
        seen = []
        for i in range(n):
            peaks.append((int(lines[i+1][0]), int(lines[i+1][2])))
            seen.append((int(lines[i+1][0]), int(lines[i+1][2])))
        print(seen)
        for f, peak in enumerate(peaks):
            for b, behind in enumerate(seen):
                if not peak == behind:
                    xfront, yfront = peak
                    xback, yback = behind
                    if yback <= (xback - xfront) + yfront and yback <= -(xback - xfront) + yfront:
                        print(peak, "in front of", behind)
                        seen.remove((behind))
                print(seen)
        print(len(seen))

    with open('mountains.out', 'w') as file:        
        file.write(str(len(seen)))


if __name__ == '__main__':
    mountains()