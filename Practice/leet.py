    
class Solution(object):
    def longestPalindrome(self, s):
        longest = 0
        values={}
        values[0] = ""
        number = 0
        for i in range(len(s)):
            number = 0
            for j in range(i, len(s)):
                number += self.hash_value(s[j], j-i)
                #print(s[i:j+1], number)
                values[(number,i,j)] = s[i:j+1]

        reverse = s[::-1]

        for i in range(len(reverse)):
            number = 0
            for j in range(i, len(reverse)):
                number += self.hash_value(reverse[j], j-i)
                if (number,len(s)-j-1,len(s)-i-1) in values.keys() and number > longest:
                    longest = number
                    ans = values[(number,len(s)-j-1,len(s)-i-1)]
        #print(values)
        #print(ans)
        return ans

   
    def character_value(self, ch):
        return (ord(ch))

    def hash_value(self, ch, size):
        return self.character_value(ch) * 200 ** (size)

                
        """
        :type s: str
        :rtype: str
        """


if __name__ == '__main__':
    s = Solution()
    print (s.longestPalindrome("aacgfcaa"))