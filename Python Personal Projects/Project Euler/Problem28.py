"""
This is the structure we're going for:
[[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0]]
"""
def printSpiral():
    for line in spiral:
        print(line)
    print()

spiral = [[1]]

currentNumber = 1
targetSpiralSize = 1001
currentTargetWidth = 1
while currentTargetWidth < targetSpiralSize:
    currentTargetWidth += 2
    for i in range(0, currentTargetWidth - 2):
        currentNumber += 1
        spiral[i].append(currentNumber)
    currentNumber += 1
    spiral.append([currentNumber])
    for i in range(1, currentTargetWidth):
        currentNumber += 1
        spiral[len(spiral) - 1].insert(0, currentNumber)
    for i in range(currentTargetWidth - 3, -1, -1):
        currentNumber += 1
        spiral[i].insert(0, currentNumber)
    currentNumber += 1
    spiral.insert(0, [currentNumber])
    for i in range(1, currentTargetWidth):
        currentNumber += 1
        spiral[0].append(currentNumber)

sum = 0
for i in range(0, 1001):
    sum += spiral[i][i] + spiral[i][1000-i]
sum -= 1
print(sum)