import math

primes = 1000000
#primes = 6

def isPrime(number):
    if number == 1:
        return False
    for i in range(2, round(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def getBinaryStr(number):
    return bin(number).replace("0b", "")

permutationsDict = {}

def getBinaryPermutations(numberLength):
    permutations = []
    currentNumber = 1
    currentBinary = getBinaryStr(currentNumber)
    while len(currentBinary) < numberLength + 1:
        if len(currentBinary) == numberLength:
            permutations.append(currentBinary)
        currentNumber += 1
        currentBinary = getBinaryStr(currentNumber)
    extraPermutations = []
    for i in permutations:
        currentBinary = "0" + i[1:]
        extraPermutations.append(currentBinary)
    permutations.extend(extraPermutations)
    permutations.remove("1" * numberLength)
    permutations.remove("0" * numberLength)
    return permutations

#Too spaghetti, need to stop writing this many nested loops and if-statements
def getAnswer(primesList):
    for number in primesList:
        if number == 56003:
            pass
        numberStr = str(number)
        strLen = len(numberStr)

        if strLen in permutationsDict:
            pass
        else:
            permutationsDict[strLen] = getBinaryPermutations(strLen)
        currentPermutations = permutationsDict[strLen]
        for replacementPoints in currentPermutations:
            currentSectionPrimes = 0
            primePermutations = []
            isValueFamily = True
            lastReplacedNumber = None
            for i in range(strLen):
                if replacementPoints[i] == '1': #Check if all the digits that are being replaced in this permutation are the same.
                    if lastReplacedNumber:
                        if lastReplacedNumber != numberStr[i]:
                            isValueFamily = False
                    else:
                        lastReplacedNumber = numberStr[i]
            if isValueFamily:
                for digit in range(0, 10):
                    
                    newNumberStr = ''
                    for i in range(strLen):
                        if replacementPoints[i] == '1':
                            newNumberStr += str(digit)
                        else:
                            newNumberStr += numberStr[i]
                    if newNumberStr[0] != '0' and isPrime(int(newNumberStr)):
                        currentSectionPrimes += 1
                        primePermutations.append(newNumberStr)
                if currentSectionPrimes == 8:
                    return numberStr, primePermutations

primesList = [2]
for i in range(0, 500000):
    currentNumber = i * 2 + 1
    if isPrime(currentNumber):
        primesList.append(currentNumber)


#print(primesList)
print("...")

print(getAnswer(primesList))
