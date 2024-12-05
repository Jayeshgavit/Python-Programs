def max_palindrom(s):
    def ispalindrom(substring):
        return substring == substring[::-1]

    max_palindrom = ' '


    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substring = s[i:j]
            if ispalindrom(substring) and len(substring) > len(max_palindrom):
                max_palindrom = substring
            
    return max_palindrom


print(max_palindrom('babad'))