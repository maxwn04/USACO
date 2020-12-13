def main():
    s = "babad"
    ans = 0
    values={}
    number = 0
    for i in range(len(s)):
        number = 0
        for j in range(i, len(s)):
            number += hash_value(s[j], j-i)
            #print(s[i:j+1], number)
            values[number] = s[i:j+1]

    reverse = s[::-1]

    for i in range(len(reverse)):
        number = 0
        for j in range(i, len(reverse)):
            number += hash_value(reverse[j], j-i)
            if number in values.keys() and number > ans:
                ans = number
    print(values)
    print (values[ans])

   
def character_value(ch):
    return (ord(ch))

def hash_value(ch, size):
    return character_value(ch) * 200 ** (size)

if __name__ == '__main__':
    main()
    