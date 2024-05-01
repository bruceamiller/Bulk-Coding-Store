# Find the first of four consecutive numbers with 4 distinct prime factors

import math

def getDistinctPrimeFactors(number):
    if number == 1:
        return
    for d in range(2, number + 1):
        if number % d == 0:
            currentPrimeFactors.add(d)
            getDistinctPrimeFactors(number // d)
            break

currentNumber = 0
consecutiveIntegers = []
consecutiveCount = 0


while consecutiveCount != 4:
    currentNumber += 1
    consecutiveCount += 1
    currentPrimeFactors = set()
    getDistinctPrimeFactors(currentNumber)

    if len(currentPrimeFactors) != 4:
        consecutiveIntegers = []
        consecutiveCount = 0
    else:
        print(currentNumber, currentPrimeFactors)
        consecutiveIntegers.append(currentNumber)


print(consecutiveIntegers[0])