# Brute force, takes too long for larger numbers
def getGridRoutes(gridSize):
    
    def breakdownRoute(rightMoves, downMoves):
        gridRoutes = 0
        if rightMoves > 0 and downMoves > 0:
            gridRoutes += breakdownRoute(rightMoves - 1, downMoves)
            gridRoutes += breakdownRoute(rightMoves, downMoves - 1)
        if rightMoves == 0 or downMoves == 0:
            gridRoutes += 1
        return gridRoutes

    return breakdownRoute(gridSize, gridSize)

def betterRoutes(gridSize):
    nodeMap = [[1] * (gridSize + 1)]
    nodeMap.extend([[0] for i in range(gridSize + 1)] for i in range(gridSize))
    for i in range(gridSize + 1):
        nodeMap[i][0] = 1

    for y in range(1, len(nodeMap)):
        for x in range(1, len(nodeMap)):
            nodeMap[y][x] = nodeMap[y][x-1] + nodeMap[y-1][x]
    return nodeMap[len(nodeMap) - 1][len(nodeMap) - 1]

def printNodes(map):
    for line in map:
        print(line)
    print()



print(betterRoutes(20))