import random, os

### Game Logic ###

def topColor(vial):
    for i in range(len(vial)-1, -1, -1): #in reverse vial?
        if vial[i] != "blank":
            return vial[i]
    return "blank"

def topPos(vial):
    top = len(vial)
    for i in range(len(vial) - 1, -1, -1): #in reverse vial?
        top -= 1
        if vial[i] != "blank":
            break
    return top

def colorDepth(vial):
    depth = 0
    color = topColor(vial)
    for i in range(topPos(vial), -1, -1):
        if vial[i] != color:
            break
        depth += 1
    return depth

def getInput():
    x = input("Input: ").split("-")
    if len(x) == 2 and x[0].isdigit() and x[1].isdigit():
        return int(x[0])-1, int(x[1])-1
    else:
        print('Please input answer as: "(#a)-(#b)"')
    return getInput()

def addLayers(vial, color, numLayers):
    startLayer = len(vial) - vial.count("blank")
    for i in range(startLayer, startLayer + numLayers):
        vial[i] = color
    return vial

def removeTopLayers(vial):
    color = topColor(vial)
    top = topPos(vial)
    for i in range(top, -1, -1):
        if vial[i] == color:
            vial[i] = "blank"
        else:
            return vial
    return vial

def checkWin(vialStore):
    for vial in vialStore:
        if vial.count(topColor(vial)) != len(vial):
            return False
    return True

### Visual Functions ###

def colorPrint(color, text):
    palette = ("blank", "red", "green", "yellow", "blue", "pink", "teal")
    print(f"\033[{palette.index(color)+30}m{text}\033[0m", end="")

def printScreen(vialStore):
    os.system('cls')
    for n, i in enumerate(vialStore):
        print(str(n+1) + "-", end="")
        for j in i:
            colorPrint(j, "#")
        print()

### Game Setup & Main Functions ###

def createVials():
    vialHeight = 4
    
    vials = 5
    blanks = 2
    filledVials = vials - blanks
    
    fillName = ["#", " ", "1", "2", "3"]
    fillName = ["background", "blank","red", "green", "blue"]
    vialStore = []
    for vial in range(filledVials):
        vialStore += [[fillName[vial + 2]] * vialHeight]
    for vial in range(blanks):
        vialStore += [["blank"] * vialHeight]
    for layer in range(vialHeight):
        tempLayer = []
        for vial in range(filledVials):
            tempLayer.append(vialStore[vial][layer])
        random.shuffle(tempLayer)
        for vial in range(filledVials):
            vialStore[vial][layer] = tempLayer[vial]            
    return vialStore

def startGame():
    vialStore = createVials()
    gameLoop(vialStore)

def gameLoop(vialStore):
    printScreen(vialStore)
    vialNum1, vialNum2 = getInput()
    if topColor(vialStore[vialNum2]) in ("blank", topColor(vialStore[vialNum1])) and vialStore[vialNum2].count("blank") >= colorDepth(vialStore[vialNum1]):
        vialStore[vialNum2] = addLayers(vialStore[vialNum2], topColor(vialStore[vialNum1]), colorDepth(vialStore[vialNum1]))
        vialStore[vialNum1] = removeTopLayers(vialStore[vialNum1])
    if checkWin(vialStore):
        printScreen(vialStore)
        print("You won!")
        if input("Would you like to play again? ").lower() in ("y", "yes"):
            startGame()
    else:
        gameLoop(vialStore)

startGame()