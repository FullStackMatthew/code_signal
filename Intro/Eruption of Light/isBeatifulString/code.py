def isBeautifulString(inputString):
    abc = [0]*26;
    for c in inputString:
        abc[ord(c) - 97] += 1
    t = len(inputString) + 1
    for i in abc:
        if t < i:
            return False
        else:
            t = i
    return True