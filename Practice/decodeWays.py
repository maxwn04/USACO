
def main(s):
    memo = {}
    ans = decodings(s,0, memo)
    print(ans)
    
    
    
def decodings(s, i, memo):
    if i in memo:
        return memo[i]
    
    if i >= len(s):
        memo[i] = 1
        return 1
    ans = 0
    
    if i+2 < len(s)+1 and int(s[i:i+2]) <= 26 and int(s[i]) > 0:
        print(i+2)
        ans += decodings(s, i+2, memo)
    if int(s[i]) > 0:        
        print(i+1)
        ans += decodings(s, i+1, memo)
    memo[i] = ans
    return ans
        
if __name__ == '__main__':
    main("0")
    """
    :type s: str
    :rtype: int
    """
    