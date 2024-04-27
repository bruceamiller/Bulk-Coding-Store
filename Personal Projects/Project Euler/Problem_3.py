

def checkPrime(number):
    highestFactor = 1
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            highestFactor = i
    if highestFactor == 1:
        return True
    else:
        return False

#I didn't expect brute force to work, lol, but still.
#largestPrime = 1
#for i in range(1, bigNumber // 2):
#    if bigNumber % i == 0 and checkPrime(i):
#        largestPrime = i

def getFirstFactor(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return i
    return 1

def getLargestPrime(bigNumber):
    largestPrime = 1
    foundLargestPrime = False
    while not foundLargestPrime:
        factor = getFirstFactor(bigNumber)
        if factor == 1:
            foundLargestPrime = True
            bigNumber = bigNumber // factor
            if bigNumber >= largestPrime and checkPrime(bigNumber):
                largestPrime = bigNumber
        elif checkPrime(factor):
            largestPrime = factor
        bigNumber = bigNumber // factor
    return(largestPrime)

if __name__ == '__main__':
    print(getLargestPrime(600851475143))