def arrayReplace(inputArray, e, s):
    return list(map(lambda x: s if x == e else x, inputArray))