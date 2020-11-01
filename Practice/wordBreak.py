def main():
    dictionary = {"i", "like", "sam", "sung", "samsung", "mobile", "ice", 
  "cream", "icecream", "man", "go", "mango"}
    s = "ilikemangogomaniiiiiiiiiiiiiiiiii"
    ans = (wordBreak(0,s,dictionary))
    print(ans)

def wordBreak(n,s,dictionary):
    if n == len(s):
        return True
    anylist = []
    for i in range(n+1,len(s)+1):
        #print(n,i,s[n:i])
        if s[n:i] in dictionary:
            
            anylist.append(wordBreak(i,s,dictionary))
    return any(anylist)


if __name__ == '__main__':
    main()