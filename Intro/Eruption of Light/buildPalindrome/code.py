def checkPalindrome(st):
    return st[::-1] == st
        
def buildPalindrome(st):
    r = st[::-1]
    if(checkPalindrome(st)):
        return st
    
    for i in range(len(st)):
        if(checkPalindrome(st + r[len(st) - i::])):
            return st + r[len(st) - i::]
    else:
        return st + r[1::]