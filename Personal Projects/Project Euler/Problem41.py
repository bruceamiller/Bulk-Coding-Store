#Find largest pandigital Prime. Pandgital = includes 1 of each digit: 1,2,3...N

import math

def isPrime(number):
    highestFactor = 1
    for i in range(2, round(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def getPermutations(head, numberStr):
    permutations = []
    if len(numberStr) == 2:
        permutations.extend([numberStr, numberStr[::-1]])
    else:
        for i in numberStr:
            for lowerPermutation in getPermutations(i, numberStr.replace(i, '')):
                permutations.append(i + lowerPermutation)
    return permutations

def getLargestPrime(strList):
    for number in strList:
        if isPrime(int(number)):
            return number


panDigits= '987654321'
leftPos = -1
gotPrime = False
while gotPrime == False:
    leftPos += 1
    permutationsList = getPermutations('', panDigits[leftPos:])
    largestPrime = getLargestPrime(permutationsList)
    if largestPrime:
        gotPrime = True

print(largestPrime)