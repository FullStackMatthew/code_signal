def sumUpNumbers(inputString):
    n = re.findall("[0-9]+",inputString)
    return sum(map(lambda x: int(x), n))