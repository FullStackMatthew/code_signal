def isMAC48Address(inputString):
    return bool(re.match('^([\dA-F]{2}-){5}([\dA-F]{2})$', inputString))