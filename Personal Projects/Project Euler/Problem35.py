#How many primes below a million are primes in every rotation of their digits?

import math

def isPrime(number):
    highestFactor = 1
    for i in range(2, round(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def inAllRotationsIsPrime(number):
    numberStr = str(number)
    for rotation in range(len(numberStr)):
        rotatedStr = numberStr[rotation:] + numberStr[:rotation]
        if not isPrime(int(rotatedStr)):
            return False
    return True

circularPrimeCount = 0
for i in range(2, 1000000):
    if inAllRotationsIsPrime(i):
        circularPrimeCount += 1

print(circularPrimeCount)