import math

def isPrime(number):
    highestFactor = 1
    for i in range(2, round(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

sum = 0
currentNumber = 2

while currentNumber <= 2000000:
    if isPrime(currentNumber):
        sum += currentNumber
    currentNumber += 1

print(sum)