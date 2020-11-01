import heapq

def convention():
    with open ('convention2.in') as file:
        lines = file.read().splitlines()
        split = lines[0].split()
        n = int(split[0])
        cowsByTime = {}
        cowsByPrio = [0]
        for i in range(n):
            split = lines[i+1].split()
            cowsByTime[int(split[0])] = i+1
            cowsByPrio.append((int(split[0]), int(split[1])))
        cowOrderTime = sorted(cowsByTime)
        #print(cowsByPrio, cowsByTime)
        time = cowOrderTime[0]
        endtime = time + cowsByPrio[cowsByTime[time]][1]
        order = [cowsByTime[time]]
        queue = []
        for i in range(n-1):
            enterTime = cowOrderTime[i+1]
            priority = cowsByTime[enterTime]
            while (enterTime > endtime and len(queue) > 0):
                curTasting = heapq.heappop(queue)
                order.append(curTasting)
                time = endtime
                endtime = time + cowsByPrio[curTasting][1]
            heapq.heappush(queue, priority)
            #queue = sorted(queue)
            #print(queue)
        for item in queue:
            order.append(item)
        #print(order)
        maxTime = 0
        time = 0
        for i in range(n):
            if cowsByPrio[order[i]][0] > time:
                time = cowsByPrio[order[i]][0]
            wait = time - cowsByPrio[order[i]][0]
            #print(wait)
            if wait > maxTime:
                maxTime = wait
            time += cowsByPrio[order[i]][1]
        print(maxTime)
    with open('convention2.out', 'w') as file:        
        file.write(str(maxTime))
if __name__ == '__main__':
    convention()