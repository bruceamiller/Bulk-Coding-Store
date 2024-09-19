import math
def isPrime(number):
    for i in range(2, round(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def printSpiral():
    for line in spiral:
        print(line)
    print()


spiral = [[1]]
totalDiagonals = 1
primeDiagonals = 0

currentNumber = 1
targetSpiralSize = 7
currentTargetWidth = 1
while True:
    currentTargetWidth += 2
    for i in range(4):
        currentNumber += currentTargetWidth - 1
        totalDiagonals += 1
        if isPrime(currentNumber):
            primeDiagonals += 1
    print(currentTargetWidth, primeDiagonals / totalDiagonals)
    if primeDiagonals / totalDiagonals < 0.1:
        print(currentTargetWidth)
        break
