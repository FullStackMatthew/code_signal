def longestDigitsPrefix(inputString):
    temp = ""
    if len(inputString) == 0: return ""
    for c in inputString:
        if(c > '9' or c < '0'): break
        else: temp += c
    return temp     