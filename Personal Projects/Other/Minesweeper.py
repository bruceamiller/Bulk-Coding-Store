import pygame, sys, random

pygame.init()

font = pygame.font.Font('freesansbold.ttf', 32)

difficultyChoice = "Expert"
difficultyNames = ["Easy", "Intermediate", "Expert"]
diffInfo = [(9, 9, 10), (16, 16, 40), (30, 16, 99)]
playWidth, playHeight, mineAmount = diffInfo[difficultyNames.index(difficultyChoice)]

SCREEN_BUFFER = 20
tileSize = 65
tileBorderWidth = 1
numberOffset = 20

SCREEN_WIDTH = tileSize * playWidth + SCREEN_BUFFER * 2
SCREEN_HEIGHT = tileSize * playHeight + SCREEN_BUFFER * 2

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Minesweeper')


def printGridList(grid):
    for line in grid:
        print(line)

def getBoardGrid():

    grid = [["0" for i in range(playWidth)] for i in range(playHeight)]

    minesInGrid = 0
    while minesInGrid < mineAmount:
        grid[random.randint(0, playHeight - 1)][random.randint(0, playWidth - 1)] = "X"
        minesInGrid = 0
        for line in grid:
            minesInGrid += line.count("X")

    for i in range(playWidth):
        for j in range(playHeight):
            if grid[j][i] == "0":
                surroundingMines = 0
                for x in range(i - 1, i + 2):
                    for y in range(j - 1, j + 2):
                        if x > -1 and y > -1 and x < playWidth and y < playHeight:
                            if grid[j][i] != grid[y][x] == "X":
                                surroundingMines += 1
                grid[j][i] = str(surroundingMines)
    return grid

hiddenGrid = getBoardGrid()
revealedGrid = [["?" for i in range(playWidth)] for i in range(playHeight)]

def printScreen():
    screen.fill(pygame.Color('black'))
    for x in range(playWidth):
        for y in range(playHeight):
            if revealedGrid[y][x] == "?":
                pygame.draw.rect(screen, pygame.Color('grey')
                                 , pygame.Rect(SCREEN_BUFFER + x * tileSize + tileBorderWidth, SCREEN_BUFFER + y * tileSize + tileBorderWidth
                                               , tileSize - tileBorderWidth * 2, tileSize - tileBorderWidth * 2))
            elif revealedGrid[y][x] == "F":
                pygame.draw.rect(screen, pygame.Color('grey')
                                 , pygame.Rect(SCREEN_BUFFER + x * tileSize + tileBorderWidth, SCREEN_BUFFER + y * tileSize + tileBorderWidth
                                               , tileSize - tileBorderWidth * 2, tileSize - tileBorderWidth * 2))                
                currentRect = pygame.draw.rect(screen, pygame.Color('black')
                                               , pygame.Rect(SCREEN_BUFFER + x * tileSize + tileBorderWidth + numberOffset
                                                             , SCREEN_BUFFER + y * tileSize + tileBorderWidth + numberOffset, 1, 1))
                currentTileText = font.render("F", True, pygame.Color('red'), pygame.Color('grey'))
                screen.blit(currentTileText, currentRect)
            elif revealedGrid[y][x] == "X":
                currentRect = pygame.draw.rect(screen, pygame.Color('black')
                                               , pygame.Rect(SCREEN_BUFFER + x * tileSize + tileBorderWidth + numberOffset
                                                             , SCREEN_BUFFER + y * tileSize + tileBorderWidth + numberOffset, 1, 1))
                currentTileText = font.render(revealedGrid[y][x], True, pygame.Color("tomato4"), pygame.Color('black'))
                screen.blit(currentTileText, currentRect)
            else:
                currentRect = pygame.draw.rect(screen, pygame.Color('black')
                                               , pygame.Rect(SCREEN_BUFFER + x * tileSize + tileBorderWidth + numberOffset
                                                             , SCREEN_BUFFER + y * tileSize + tileBorderWidth + numberOffset, 1, 1))
                if revealedGrid[y][x] != "0":
                    colorPos = int(revealedGrid[y][x])
                    colors = ["white", "blue", "green4", "red2", "blue4", "red4", "cyan4", "black", "light slate gray"]
                    currentTileText = font.render(revealedGrid[y][x], True, pygame.Color(colors[colorPos]), pygame.Color('black'))
                    screen.blit(currentTileText, currentRect)
    pygame.display.update()

def revealTile(pos, currentRevealedTiles = []):
    mouseX = pos[0]
    mouseY = pos[1]
    x = (mouseX - tileBorderWidth - SCREEN_BUFFER) // tileSize
    y = (mouseY - tileBorderWidth - SCREEN_BUFFER) // tileSize
    if revealedGrid[y][x] == "?":
        revealedGrid[y][x] = hiddenGrid[y][x]
        currentRevealedTiles = currentRevealedTiles + [[x, y]]
        newTiles = True
        while newTiles:
            newTiles = False
            for tile in currentRevealedTiles:
                currentX = tile[0]
                currentY = tile[1]
                if revealedGrid[currentY][currentX] == "0":
                    for i in range(currentX-1, currentX + 2):
                        for j in range(currentY-1, currentY + 2):
                            if i > -1 and j > -1 and i < playWidth and j < playHeight:
                                if not [i, j] in currentRevealedTiles:
                                    newTiles = True
                                    currentRevealedTiles.append([i, j])
                                    revealedGrid[j][i] = hiddenGrid[j][i]
        return hiddenGrid[y][x]


def flagTile(pos):
    mouseX = pos[0]
    mouseY = pos[1]
    x = (mouseX - tileBorderWidth - SCREEN_BUFFER) // tileSize
    y = (mouseY - tileBorderWidth - SCREEN_BUFFER) // tileSize
    if revealedGrid[y][x] == "?":
        revealedGrid[y][x] = "F"
    elif revealedGrid[y][x] == "F":
        revealedGrid[y][x] = "?"


pastFirstMove = False
gameEnd = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not gameEnd:
            pos = pygame.mouse.get_pos()
            buttonStore = pygame.mouse.get_pressed()
            buttonPressed = None
            if buttonStore.count(True) == 1:
                buttonPressed = buttonStore.index(True)
            if buttonPressed == 0: #Leftclick
                while not pastFirstMove:
                    if revealTile(pos) == "0":
                        pastFirstMove = True
                    else:
                        hiddenGrid = getBoardGrid()
                        revealedGrid = revealedGrid = [["?" for i in range(playWidth)] for i in range(playHeight)]
                if revealTile(pos) == "X":
                    gameEnd = True
                    print("EXPLODED")
            if buttonPressed == 2: #Rightclick
                flagTile(pos)
    
    hiddenMines = 0
    onlyMines = True
    for x in range(playWidth):
        for y in range(playHeight):
            if revealedGrid[y][x] in ("?", "F"):
                if hiddenGrid[y][x] == "X":
                    hiddenMines += 1
                else:
                    onlyMines = False
    if hiddenMines == mineAmount and onlyMines:
        gameEnd = True
        print("You win!")
        revealedGrid = hiddenGrid
    printScreen()