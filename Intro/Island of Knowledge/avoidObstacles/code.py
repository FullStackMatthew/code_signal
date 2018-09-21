def avoidObstacles(inputArray):
    for i in range(2,42):
        t = True
        for n in inputArray:
            t = t and (n%i != 0)
        if t: return i