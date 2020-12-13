#code


def main():
    memo = {}
    print (cat(5,memo))
    
    
def cat(n, memo):
    if n in memo:
        return memo[n]
    if n == 0:
        memo[0] = 1
        return memo[0]
    val = 0
    for i in range(n):
        val += cat(i,memo) * cat(n-1-i,memo)
    memo[n] = val
    return memo[n]
        


if __name__ == '__main__':
	main()