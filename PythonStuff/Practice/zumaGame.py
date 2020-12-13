def main():
    n = [2, 3, 5, 6, 1, 1, 1, 1, 6, 4]
    pn = ridOfOnes(n)
    print(pn)
    
# def eliminate(s):
        
#         #print("cancelling " + s)
#         s = s + ' '
#         prev = ''
#         inARow = 1
#         sNew = ''
#         for i,item in enumerate(s):
#             #print(i,item,inARow)
#             if item == prev:
#                 inARow += 1
#             elif inARow >= 3:
#                 #print("cancelling")
#                 sNew = s[0:i-inARow] + s[i:len(s)]
#                 inARow = 1
#                 break
#             else:
#                 inARow = 1
#             prev = item

        

#         if not sNew == '':
#             sNew = eliminate(sNew)
#         else:
#             sNew = s
#         #print(sNew)
#         return sNew.strip()

# def same(s):
#     prev = s[0]
#     for item in s:
#         if not prev == item :
#             return s
#     return ''


def ridOfOnes(n):
        pn = []
        counter = 0
        while counter < len(n):
            if n[counter] == 1:
                counter += 1
            elif counter + 1 < len(n):
                if n[counter] == n[counter +1] and n[counter] == -1:
                    counter += 2
            else:
                pn.append(n[counter])
                counter += 1

        return pn
            

if __name__ == '__main__':
    main()
