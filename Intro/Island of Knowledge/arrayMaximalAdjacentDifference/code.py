def arrayMaximalAdjacentDifference(a):
        return max([abs(a[i]-a[i+1]) for i in range(len(a)-1)])