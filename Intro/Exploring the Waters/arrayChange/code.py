def arrayChange(inputArray):
    last = inputArray[0] - 1
    c = 0
    for i in inputArray:
        last = max(last + 1, i)
        c += last - i
    return c