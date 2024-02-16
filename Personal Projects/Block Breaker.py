import pygame, sys, random

pygame.init()

framerate = 60
paddleSpeed = framerate // 5
ballSpeed = framerate // 15
clock = pygame.time.Clock()

screenHeight = 750
screenWidth = screenHeight  * 2
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Pong')

paddleSize = [screenHeight // 4, screenHeight // 100]
paddlePos = [screenWidth // 2 - paddleSize[0] // 2, screenHeight * 9 // 10]
paddleDirection = 'STOP'

ballSize = screenHeight // 50

ballInfo = [paddlePos[0], screenHeight * 8 // 10, 'DOWNRIGHT']

bricksTop = screenHeight // 10
bricksDepth = screenHeight * 4 // 10
xBlocks = 10
yBlocks = 5
buffer = screenHeight // 75
blockWidth = (screenWidth - buffer * (xBlocks + 1)) // xBlocks
blockHeight = (bricksDepth - buffer * (yBlocks)) // yBlocks
blockStore = []
for x in range(0, xBlocks):
    xPos = buffer + (blockWidth + buffer) * x
    for y in range(0, yBlocks):
        yPos = bricksTop + (blockHeight + buffer) * y
        blockStore.append([xPos, yPos])

def printScreen():
    screen.fill(pygame.Color('black'))
    pygame.draw.rect(screen, pygame.Color('white'), pygame.Rect(paddlePos[0], paddlePos[1], paddleSize[0], paddleSize[1]))
    for block in blockStore:
        pygame.draw.rect(screen, pygame.Color('grey'), pygame.Rect(block[0], block[1], blockWidth, blockHeight))
    pygame.draw.ellipse(screen, pygame.Color('white'), pygame.Rect(ballInfo[0], ballInfo[1], ballSize, ballSize))
    pygame.display.update()

def movePaddle(paddlePos):
    if paddleDirection == 'LEFT' and paddlePos[0] >= 0:
        paddlePos[0] -= paddleSpeed
    elif paddleDirection == 'RIGHT' and paddlePos[0] <= screenWidth - paddleSize[0]:
        paddlePos[0] += paddleSpeed
    return paddlePos

def changeDirection(ballDirection, newDirection):
    normalDirections = ['UP', 'DOWN', 'LEFT', 'RIGHT']
    oppositeDirections = ['DOWN', 'UP', 'RIGHT', 'LEFT']
    ballDirection = ballDirection.replace(oppositeDirections[normalDirections.index(newDirection)], newDirection)
    return ballDirection

def moveBall(ballInfo):
    if 'UP' in ballInfo[2]:
        ballInfo[1] -= ballSpeed
    elif 'DOWN' in ballInfo[2]:
        ballInfo[1] += ballSpeed
    if 'LEFT' in ballInfo[2]:
        ballInfo[0] -= ballSpeed
    elif 'RIGHT' in ballInfo[2]:
        ballInfo[0] += ballSpeed
    return ballInfo

def closestBlocks(ballInfo, blockStore):
    blocks = []
    closeX = blockWidth
    closeY = blockHeight
    for block in blockStore:
        if block[0] >= ballInfo[0] - closeX and block[0] + blockWidth <= ballInfo[0] + ballSize + closeX and block[1] >= ballInfo[1] - closeY and block[1] + blockHeight <= ballInfo[1] + ballSize + closeY:
            blocks.append(block)
    return blocks

def ballCollision(ballInfo, blockStore):
    blocks = closestBlocks(ballInfo, blockStore)
    remove = []
    if ballInfo[1] >= paddlePos[1] - ballSize and ballInfo[1] + ballSize <= paddlePos[1] + paddleSize[1] and ballInfo[0] - ballSize + 1 >= paddlePos[0] and ballInfo[0] - 1 <= paddlePos[0] + paddleSize[0]:
        ballInfo[2] = changeDirection(ballInfo[2], 'UP')
        if ballInfo[0] - ballSize + 1 >= paddlePos[0] and ballInfo[0] - 1 <= paddlePos[0] + paddleSize[0] // 3:
            ballInfo[2] = changeDirection(ballInfo[2], 'LEFT')
        elif ballInfo[0] - ballSize + 1 >= paddlePos[0] + paddleSize[0] * 2 // 3 and ballInfo[0] - 1 <= paddlePos[0] + paddleSize[0]:
            ballInfo[2] = changeDirection(ballInfo[2], 'RIGHT')
    if ballInfo[0] <= 0:
        ballInfo[2] = changeDirection(ballInfo[2], 'RIGHT')
    if ballInfo[0] >= screenWidth - ballSize:
        ballInfo[2] = changeDirection(ballInfo[2], 'LEFT')
    if ballInfo[1] <= 0:
        ballInfo[2] = changeDirection(ballInfo[2], 'DOWN')
    if ballInfo[1] >= screenHeight:
        ballInfo = [paddlePos[0], screenHeight * 8 // 10, 'DOWNRIGHT']        
    for block in blocks:
        #over[Direction that the ball moved to overlap with the block]
        overDown = ballInfo[1] + ballSize - block[1]
        overUp = block[1] + blockHeight - ballInfo[1]
        overRight = ballInfo[0] + ballSize - block[0]
        overLeft = block[0] + blockWidth - ballInfo[0]
        inBlock = False
        if overDown > 0 and overUp > 0 and overRight > 0 and overLeft > 0:
            inBlock = True
        if inBlock:
            if overUp <= overDown and overUp <= overLeft and overUp <= overRight:
                ballInfo[2] = changeDirection(ballInfo[2], 'DOWN')
                remove.append(block)
            elif overDown <= overUp and overDown <= overLeft and overDown <= overRight:
                ballInfo[2] = changeDirection(ballInfo[2], 'UP')
                remove.append(block)
            elif overLeft <= overRight and overLeft <= overUp and overLeft <= overDown:
                ballInfo[2] = changeDirection(ballInfo[2], 'RIGHT')
                remove.append(block)
            elif overRight <= overLeft and overRight <= overUp and overRight <= overDown:
                ballInfo[2] = changeDirection(ballInfo[2], 'LEFT')
                remove.append(block)
    for block in remove:
        blockStore.remove(block)
    return ballInfo, blockStore

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_LEFT:
                paddleDirection = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                paddleDirection = 'RIGHT'
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and paddleDirection == 'LEFT':
                paddleDirection = 'STOP'
            elif event.key == pygame.K_RIGHT and paddleDirection == 'RIGHT':
                paddleDirection = 'STOP'
    paddlePos = movePaddle(paddlePos)
    ballInfo, blockStore = ballCollision(ballInfo, blockStore)
    ballInfo = moveBall(ballInfo)
    printScreen()
    if not blockStore:
        print("You won!")
        pygame.quit()
        break
    clock.tick(framerate)
