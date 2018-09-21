def addDigits(n, m):
    if n < 10:
        return m;
    else:
        t = 0;
        while(n > 0):
            t += n % 10
            n //= 10
        return addDigits(t, m + 1);

def digitDegree(n):
    return addDigits(n, 0)