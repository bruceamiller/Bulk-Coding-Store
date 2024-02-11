import pygame, sys, random

pygame.init()

framerate = 60
speed = framerate // 10
clock = pygame.time.Clock()

screenHeight = 1000
screenWidth = screenHeight // 2

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Rise and Fall')

playerSize = [50, 100]
playerInfo = [screenWidth // 2 - playerSize[0] // 2, screenHeight, 0] #x_left, y_bottom, upSpeed
move = 'STOP'

def movePlayer(playerInfo, move):
    if move == 'LEFT':
        playerInfo[0] -= speed
    if move == 'RIGHT':
        playerInfo[0] += speed
    if move == 'UP' and playerInfo[1] == screenHeight:
        playerInfo[2] = speed * 40
        playerInfo[1] -= playerInfo[2] // speed + 1
    elif playerInfo[1] < screenHeight:
        playerInfo[2] -= speed
        playerInfo[1] -= playerInfo[2] // speed + 1
    else:
        playerInfo[2] = 0
        playerInfo[1] = screenHeight

    return playerInfo

def printScreen(playerInfo):
    screen.fill(pygame.Color('black'))
    player = pygame.Rect(0, 0, playerSize[0], playerSize[1])
    player.bottomleft = (playerInfo[0], playerInfo[1] - playerSize[1] // 2)
    pygame.draw.rect(screen, pygame.Color('white'), player)
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                move = 'UP'
            if event.key == pygame.K_RIGHT:
                move = 'RIGHT'
            if event.key == pygame.K_LEFT:
                move = 'LEFT'
        if event.type == pygame.KEYUP:
            move = 'STOP'
    playerInfo = movePlayer(playerInfo, move)
    printScreen(playerInfo)
    clock.tick(framerate)