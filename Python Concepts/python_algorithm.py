#Algorithm for Palindrom

def isPalindrom(str):
    startIndex = 0
    endIndex = len(str) - 1 
    
    for x in str:
        if str[startIndex] != str[endIndex]:
            return('This is not palindrom')
        return ('This is palindrom')
    
    print(isPalindrom('racecar'))
    print(isPalindrom('racecars'))
