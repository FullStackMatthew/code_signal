def checkPalindrome(inputString):
    reverseString = inputString[::-1]

    if(inputString == reverseString):
        return True
    else:
        return False