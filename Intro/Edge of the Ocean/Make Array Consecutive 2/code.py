def makeArrayConsecutive2(statues):
    statues.sort()
    missing = 0
    for i in range(0, len(statues) - 1):
        missing += statues[i + 1] - statues[i] - 1
    else:
        return missing