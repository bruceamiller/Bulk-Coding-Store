import math
#Use immutable sets? frozenset()

rightTriangleSets = set()

for a in range(1, 1000):
    for b in range(1, 1000-a):
        c = math.sqrt(a ** 2 + b ** 2)
        if c == int(c) and a + b + c <= 1000:
            newSet = frozenset([a, b, int(c)])
            rightTriangleSets.add(newSet)

pCount = [0 for i in range(1001)]
for set in rightTriangleSets:
    p = 0
    for number in set:
        p += number
    pCount[p] += 1

highestSolutions = 0
highestIndex = 0

for i, solutionCount in enumerate(pCount):
    if solutionCount > highestSolutions:
        highestSolutions = solutionCount
        highestIndex = i

print(highestIndex)