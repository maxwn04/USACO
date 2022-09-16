def main():
    alist = {0: [1, 2, 5], 1: [4, 11], 2: [9, 5, 16], 3: [2], 4: [18], 5: [13], 6: [2], 7: [], 
        8: [], 9: [], 10: [], 11: [], 13: [], 16:[], 18: []}
    memo = []
    print(dfs(0, alist, memo))
    print(memo)
    # memo = []
    # print(bfs(0, alist, memo))


def dfs(n, alist, memo):
    
    if n in memo:
        return 0

    if len(alist[n]) == 0:
        memo.append(n)
        return 0

    ans = 1
    for i in range(len(alist[n])):
        ans += dfs(alist[n][i], alist, memo)
        
    memo.append(n)
    return ans
    

def bfs(node, alist, memo):
    queue = [node]
    been = {}
    ans = 0
    for node in queue:
        if node not in been:
            ans += 1
            been[node] = 1
            for item in alist[node]:
                queue.append(item)
    memo[node] = ans
    return ans


if __name__ == '__main__':
    main()