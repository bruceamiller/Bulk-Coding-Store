def getMax(myList):
    if len(myList) > 0:
        if len(myList) == 1:
            return myList[0]
        lowerMax = getMax(myList[1:])
        if myList[0] >= lowerMax:            
            return myList[0]
        else:
            return lowerMax

def getSum(myList):
    if len(myList) == 0:
        return 0
    else:
        return myList[0] + getSum(myList[1:])

def revList(myList):
    if len(myList) > 0:
        newList = revList(myList[1:])
        newList.append(myList[0])
        return newList
    else:
        return []

def isPrime(n, d=2):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % d == 0:
        return False
    elif n > d + 1:
        return isPrime(n, d + 1)
    else:
        return True

def getPrimeFactors(n, d=2):
    if n % d == 0:
        print(d, end=" ")
        return getPrimeFactors(n // d, d)
    elif n > d:
        return getPrimeFactors(n, d + 1)


#print(getMax([1, 2, 3, 4]))
#print(revList([1, 2, 3, 4]))
#print(getSum([1, 2, 3, 4]))
#print(isPrime(7))
getPrimeFactors(36)