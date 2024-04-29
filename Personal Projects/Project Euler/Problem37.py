#What is the sum of the 11 prime numbers > 7 that can be truncated any number of times from either left or right, yet remain prime.

import math

def isPrime(number):
    highestFactor = 1
    for i in range(2, round(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    if number > 1:
        return True
    return False

def reverseString(string):
    reversedText = ""
    for digit in reversed(string):
        reversedText += digit
    return reversedText

i = 10
truncatedPrimes = []
while len(truncatedPrimes) < 11:
    i += 1
    print(i)

    numberString = str(i)    
    continuousPrime = True
    for split in range(len(numberString)):
        splitNumber = int(numberString[split:])
        if not isPrime(splitNumber):
            continuousPrime = False

    for split in range(len(numberString)):
        splitNumber = int(numberString[:len(numberString) - split])
        if not isPrime(splitNumber):
            continuousPrime = False

    if continuousPrime:
        truncatedPrimes.append(i)

print(truncatedPrimes)
print(sum(truncatedPrimes))

#499999499955, 4999949955, 49994955, 499455, 4905