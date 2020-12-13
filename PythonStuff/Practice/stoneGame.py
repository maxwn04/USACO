def stoneGameII(self, piles):
        memo = {}
        piles = [2,7,9,4,4]
        return self.alexScore(1, 1, 1, piles, memo)
    
    
def alexScore(self, start, m, alexTurn, piles, memo):
    if (start,m,turn) in memo:
        return memo[(start,m,turn)]
    
    if start == len(piles):
        memo[(start,m,turn)] = 0
        return 0
    
    scores = []
    curTurn = 0
    for x in range(min(2m, len(piles) - start)):
        curTurn += piles[start+x]
        scores.append(curTurn + self.alexScore(start+i, max(m,x), -alexTurn, piles, memo))
        
    ans = 0
    if alexTurn > 0:
        ans = max(scores)
    else:
        ans = min(scores)
    memo[(start,m,turn)] = ans
    
    return ans