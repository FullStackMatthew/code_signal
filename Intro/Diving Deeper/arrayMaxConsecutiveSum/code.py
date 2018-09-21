def arrayMaxConsecutiveSum(inputArray, k):
    s0 = sum(inputArray[:k])
    s1 = s0
    for i in range(1,len(inputArray) - k + 1):
        s1 = s1 - inputArray[i-1] + inputArray[i+k-1]
        if s1 > s0: s0 = s1
    return s0