file = open("C:\\Users\\Bruce\\Documents\\GitHub\\Python-Coding\\Personal Projects\\Project Euler\\Problem18.txt")

numPyramid = []
for line in file.readlines():
    line = line.split()
    for i in range(len(line)):
        line[i] = int(line[i])
    numPyramid.append(line)
file.close
print(numPyramid)
pyrHeight = len(numPyramid)


def moveRight(node):
    newNode = list(node)
    newNode[1] += 1
    return newNode
def leftDownNode(node):
    newNode = list(node)
    newNode[0] += 1
    return newNode
def canMoveRight(topNode, mainNode):
    if topNode and topNode[1] == mainNode[1]:
        return True
    return False
def calcNew(highestSum):
    adjacentSum = 0
    for node in nodeStack:
        adjacentSum += numPyramid[node[0]][node[1]]
    if adjacentSum > highestSum:
        highestSum = adjacentSum
    print(nodeStack)
    return highestSum

nodeStack = [[x, 0] for x in range(0, pyrHeight)]
newStack = True

highestSum = 0
highestSum = calcNew(highestSum)
lastStack = None
while nodeStack != lastStack:
    lastStack = list(nodeStack)

    for stack in range(pyrHeight - 1, 0, -1):
        if canMoveRight(nodeStack[stack - 1], nodeStack[stack]):
            nodeStack[stack] = moveRight(nodeStack[stack])
            #Move all lower nodes to the left of right-moved node.
            for fallstack in range(stack, pyrHeight - 1):
                nodeStack[fallstack + 1] = leftDownNode(nodeStack[fallstack])
            break
    
    highestSum = calcNew(highestSum)


    
            
print(highestSum, newStack, nodeStack)