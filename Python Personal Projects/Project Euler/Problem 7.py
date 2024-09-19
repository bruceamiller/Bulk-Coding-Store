from Problem_3 import *

primeCount = 0
currentNumber = 2

while primeCount != 10001:
    if currentNumber == getLargestPrime(currentNumber):
        lastPrime = currentNumber
        primeCount += 1
    currentNumber += 1
    

print(lastPrime)