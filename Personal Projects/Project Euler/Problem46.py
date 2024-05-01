import math

def isPrime(number):
    highestFactor = 1
    for i in range(2, round(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

primes = []

currentNumber = -1
canBeSummed = True
while canBeSummed:
    canBeSummed = False
    currentNumber += 2

    if isPrime(currentNumber):
        primes.append(currentNumber)
    
    for p in primes[:len(primes)]:
        squaredNum = (currentNumber - p) // 2
        unSquaredNum = math.sqrt(squaredNum)
        if unSquaredNum == int(unSquaredNum):
            canBeSummed = True


print(currentNumber)