file = open("C:\\Users\\Bruce\\Documents\\GitHub\\Python-Coding\\Personal Projects\\Project Euler\\Problem11.txt")

def getNumGrid():
    file = open("C:\\Users\\Bruce\\Documents\\GitHub\\Python-Coding\\Personal Projects\\Project Euler\\Problem11.txt")
    numGrid = []
    for line in file.readlines():
        newLine = []
        line = line.split()
        for number in line:
            newLine.append(int(number))
        numGrid.append(newLine)
    file.close()
    return numGrid

def listProduct(list):
    product = 1
    for num in list:
        product *= num
    return product


numGrid = getNumGrid()
print(numGrid)

greatestProduct = 0

# Check horizontal adjacent 4's
for line in numGrid:
    for numberLeft in range(len(line) - 3):
        newQuart = []
        for rightMove in range(4):
            newQuart.append(line[numberLeft + rightMove])
        if listProduct(newQuart) > greatestProduct:
            greatestProduct = listProduct(newQuart)

# Check vertical adjacent 4's
for linePos in range(len(numGrid[0])):
    for numberTop in range(len(numGrid) - 3):
        newQuart = []
        for downMove in range(4):
            newQuart.append(numGrid[numberTop + downMove][linePos])
        if listProduct(newQuart) > greatestProduct:
            greatestProduct = listProduct(newQuart)

# Check -45 Diagonal adjacent 4's
for linePos in range(len(numGrid[0])-3):
    for numberTop in range(len(numGrid) - 3):
        newQuart = []
        for diagonalMove in range(4):
            newQuart.append(numGrid[numberTop + diagonalMove][linePos + diagonalMove])
        if listProduct(newQuart) > greatestProduct:
            greatestProduct = listProduct(newQuart)

# Check +45 Diagonal adjacent 4's
for linePos in range(3, len(numGrid[0])):
    for numberTop in range(len(numGrid) - 3):
        newQuart = []
        for diagonalMove in range(4):
            newQuart.append(numGrid[numberTop + diagonalMove][linePos - diagonalMove])
        if listProduct(newQuart) > greatestProduct:
            greatestProduct = listProduct(newQuart)

print(greatestProduct)