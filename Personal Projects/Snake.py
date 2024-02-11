import pygame, sys, random

pygame.init()

gridWidth = 20
gridHeight = 15
cellSize = 50
width, height = ((gridWidth+1) * cellSize), ((gridHeight+1) * cellSize)
framerate = 8
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()


snakeBody, snakeDirection, alive =[[0, 2], [1, 2], [2, 2], [3, 2]], 'RIGHT', True

def getApple(snakeBody):
    applePos = list((random.randint(0, gridWidth), random.randint(0, gridHeight)))
    for i in snakeBody:
        if applePos == i:
            applePos = getApple(snakeBody)
            break
    return applePos

appleLocation = getApple(snakeBody)
print(appleLocation)

def moveSnakeDirection(newHead, snakeDirection):
    if snakeDirection == 'UP':
        newHead[1] -= 1
    elif snakeDirection == 'RIGHT':
        newHead[0] += 1
    elif snakeDirection == 'DOWN':
        newHead[1] += 1
    elif snakeDirection == 'LEFT':
        newHead[0] -= 1
    return newHead

def snakeLoop(snakeBody, snakeDirection, appleLocation):
    newHead = list(snakeBody[len(snakeBody)-1])
    newHead = moveSnakeDirection(newHead, snakeDirection)
    if newHead == snakeBody[len(snakeBody)-2]:
        normalDir = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        flipDir = ['DOWN', 'UP', 'RIGHT', 'LEFT']
        newHead = list(snakeBody[len(snakeBody)-1])
        snakeDirection = flipDir[normalDir.index(snakeDirection)]
        newHead = moveSnakeDirection(newHead, snakeDirection)
    snakeBody.append(newHead)
    if newHead != list(appleLocation):
        snakeBody.pop(0)
    else:
        appleLocation = getApple(snakeBody)
    return snakeBody, appleLocation

def deathCheck(snakeBody):
    snakeHead = snakeBody[len(snakeBody)-1]
    for snakeSegment in snakeBody[0:(len(snakeBody)-2)]:
        if snakeHead == snakeSegment:
            return False
    if snakeHead[0] in (-1, gridWidth + 1) or snakeHead[1] in (-1, gridHeight + 1):
        return False
    return True

def printScreen(snakeBody, appleLocation):
    screen.fill(pygame.Color('black'))
    for i in snakeBody:
        pygame.draw.rect(screen, pygame.Color('white'), pygame.Rect(i[0] * cellSize, i[1] * cellSize, cellSize, cellSize))
    pygame.draw.rect(screen, pygame.Color('red'), pygame.Rect(appleLocation[0] * cellSize, appleLocation[1] * cellSize, cellSize, cellSize))
    pygame.display.update()

def gameLoop(snakeBody, appleLocation, snakeDirection):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                snakeDirection = 'UP'
            if event.key == pygame.K_RIGHT:
                snakeDirection = 'RIGHT'
            if event.key == pygame.K_DOWN:
                snakeDirection = 'DOWN'
            if event.key == pygame.K_LEFT:
                snakeDirection = 'LEFT'
    snakeBody, appleLocation = snakeLoop(snakeBody, snakeDirection, appleLocation)
    alive = deathCheck(snakeBody)
    printScreen(snakeBody, appleLocation)
    clock.tick(framerate)
    if alive:
        gameLoop(snakeBody, appleLocation, snakeDirection)
    else:
        return print("You died!")
gameLoop(snakeBody, appleLocation, snakeDirection)