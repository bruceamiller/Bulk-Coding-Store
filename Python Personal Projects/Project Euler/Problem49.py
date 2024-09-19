import math

def isPrime(number):
    try:
        for i in range(2, round(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
    except:
        pass
    return True

def allIsPrime(numList):
    for i in numList:
        if not isPrime(i):
            return False
    return True

def getNumberCount(str):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    numberCount = [0 for x in range(10)]
    for i in str:
        numberCount[numbers.index(i)] += 1
    return numberCount

def areEqualPermutations(numList):
    strList = []
    for i in numList:
        strList.append(str(i))
    for i in range(1, len(strList)):
        if getNumberCount(strList[i]) != getNumberCount(strList[i - 1]):
            return False
    return True


concatenatedStrings = []
for i in range(1000, 9999):
    j = i + 3330
    k = j + 3330
    if allIsPrime([i, j, k]) and areEqualPermutations([i, j, k]) and i != j != k:
        concatenatedStrings.append(str(i) + str(j) + str(k))

print(concatenatedStrings)
