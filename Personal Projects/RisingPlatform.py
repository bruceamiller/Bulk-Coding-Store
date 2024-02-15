import pygame, sys, random

pygame.init()

framerate = 60
speed = framerate // 10
acceleration = speed * 2
clock = pygame.time.Clock()

screenHeight = 1000
screenWidth = screenHeight // 2

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Rise and Fall')


wallbuffer = screenHeight // 100
platformWidth = screenHeight // 10
platformDepth = screenHeight // 200
platformDistance = screenHeight // 6
platformTypes = ['normal'] * 20 + ['moving1', 'moving2', 'falling0'] * 3 + ['bounce']

playerSize = [screenHeight // 20, screenHeight // 10]

font = pygame.font.Font('freesansbold.ttf', 16)
score = 0
scoreBoard = font.render(f"Height: {score}", True, pygame.Color('grey'), pygame.Color('black'))
scoreBoardRect = scoreBoard.get_rect()
scoreBoardRect.topleft = (wallbuffer, wallbuffer * 5)

def getPlatformHorizontal():
    return random.randint(wallbuffer, screenWidth - wallbuffer - platformWidth)

def getPlatformType():
    return random.choice(platformTypes)


def closestPlatform(playerInfo, platforms):
    output = []
    playerY = playerInfo[1]
    lowestDistance = -10000 #arbitrarily large number
    # check for closest platform below player
    for platform in platforms:
        distance = platform[1] - playerY
        if distance <= 0 and distance > lowestDistance:
            output = platform
            lowestDistance = playerY - output[1]
    #if no lower platform, check for closest platform above player~
    if output:
        return output
    else:
        lowestDistance = 10000
        distance = playerY - platform[1]
        if distance < lowestDistance:
            output = platform
            lowestDistance = playerY - output[1]
        return output

platforms = []
platformTotal = 1
for height in range(screenHeight - playerSize[1], 0 - playerSize[1], -platformDistance):
    platformTotal += 1
    newPlatform = [getPlatformHorizontal(), height, platformTypes[0]]
    platforms.append(newPlatform)

playerInfo = [screenWidth // 2 - playerSize[0] // 2, screenHeight, 0] #x_left, y_bottom, upSpeed
playerInfo = closestPlatform(playerInfo, platforms)[0:2] + [0]
playerInfo[0] += platformWidth // 2 - playerSize[0] // 2
move = 'STOP'

def onPlatformY(playerInfo, platform):
    if  platform[1] + playerSize[1] // 2 <= playerInfo[1]  <= platform[1] + platformWidth // 5 + playerSize[1] // 2:
        return True
    return False

def onPlatformX(playerInfo, platform):
    if platform[0] - platformWidth // 2 < playerInfo[0] < platform[0] + platformWidth:
        return True
    return False

def displacement(playerY, playerSpeed):
    return playerY - playerSpeed // acceleration

def movePlayer(playerInfo, move, platforms):
    platform = closestPlatform(playerInfo, platforms)
    if 'LEFT' in move:
        playerInfo[0] -= speed
    if 'RIGHT' in move:
        playerInfo[0] += speed
    # jump if pressing up, and player either on bottom of screen or on platform
    if 'UP' in move and (playerInfo[1] == screenHeight or (onPlatformY(playerInfo, platform) and playerInfo[2] == 0)):
        playerInfo[2] = speed * 40
        playerInfo[1] = displacement(playerInfo[1], playerInfo[2])
    # apply gravity to player if either not on platform x and y or if player is moving upwards (Hotfix* - so long as negative player speed is not too fast)
    #(Too high speed clips through bottom platform, because player is still close to or above top platform Fix?)
    #negative speed cannot be faster than platform gap... Fix! Find which platform is actually underneath it at all times?
    elif playerInfo[1] < screenHeight and (not (onPlatformX(playerInfo, platform) and onPlatformY(playerInfo, platform)) or playerInfo[2] > 0) and playerInfo[2] >= -100:
        playerInfo[2] -= speed
        playerInfo[1] = displacement(playerInfo[1], playerInfo[2])
    elif onPlatformX(playerInfo, platform) and playerInfo[1] - playerSize[1] * 2 // 3 <= platform[1] and displacement(playerInfo[1], playerInfo[2]) >= platform[1] and playerInfo[2] <= 0:
        playerInfo[2] = 0
        playerInfo[1] = platform[1] + playerSize[1] // 2
        if platform[2] == 'falling0':
            platforms[platforms.index(platform)][2] = 'falling1'
            print(platforms, platforms.index(platform))
    else:
        playerInfo[1] = displacement(playerInfo[1], playerInfo[2])
    if 'UP' in move and onPlatformX(playerInfo, platform) and platform == closestPlatform(playerInfo, platforms) and onPlatformY(playerInfo, platform) and platform[2] == 'falling1':
        playerInfo[2] = speed * 40
        playerInfo[1] = displacement(playerInfo[1], playerInfo[2])
    elif onPlatformX(playerInfo, platform) and platform == closestPlatform(playerInfo, platforms) and onPlatformY(playerInfo, platform) and platform[2] == 'bounce' and playerInfo[2] <= 0:
        playerInfo[2] = speed * 100
        playerInfo[1] = displacement(playerInfo[1], playerInfo[2])
    return playerInfo, platforms

def movePlatforms(platforms):
    for platform in platforms:
        if platform[2] == 'moving1':
            if platform[0] >= screenWidth - wallbuffer - platformWidth:
                platform[2] = 'moving2'
            else:
                platform[0] += speed // 2
        elif platform[2] == 'moving2':
            if platform[0] <= wallbuffer:
                platform[2] = 'moving1'
            else:
                platform[0] -= speed // 2
        elif platform[2] == 'falling0' and playerInfo[0] == platform[0] and playerInfo[2] <= 0:
            platform[2] == 'falling1'
        elif platform[2] == 'falling1':
            platform[1] += speed // 2
    return platforms, playerInfo

def moveScreen(playerInfo, platforms, score):
    aboveScreen = playerInfo[1] - playerSize[1] - screenHeight // 4
    if aboveScreen <= 0:
        for platform in platforms:
            platform[1] -= aboveScreen
        playerInfo[1] -= aboveScreen
        score -= aboveScreen // 100
    #Deletes platforms that go off screen and create new platforms
    for platform in platforms:
        if platform[1] > screenHeight:
            platforms.pop(platforms.index(platform))
            heighestPlatform = [0, 0]
            for platform in platforms:
                if platform[1] <= heighestPlatform[1]:
                    heighestPlatform = platform
            newplatform = [getPlatformHorizontal(), heighestPlatform[1] - platformDistance, getPlatformType()]
            platforms.append(newplatform)
    #Move to other side if goes off screen
    if playerInfo[0] > screenWidth:
        playerInfo[0] -= screenWidth
    elif playerInfo[0] < 0:
        playerInfo[0] += screenWidth
    return playerInfo, platforms, score

def printScreen(playerInfo, platforms, scoreBoard, scoreBoardRect):
    screen.fill(pygame.Color('black'))
    player = pygame.Rect(0, 0, playerSize[0], playerSize[1])
    player.bottomleft = (playerInfo[0], playerInfo[1] - playerSize[1] // 2)
    for platform in platforms:
        if platform[2] == 'normal':
            pygame.draw.rect(screen, pygame.Color('grey'), pygame.Rect(platform[0], platform[1], platformWidth, platformDepth))
        elif platform[2] == 'moving1' or platform[2] == 'moving2':
            pygame.draw.rect(screen, pygame.Color('red'), pygame.Rect(platform[0], platform[1], platformWidth, platformDepth))
        elif platform[2] == 'falling0' or platform[2] == 'falling1':
            pygame.draw.rect(screen, pygame.Color('blue'), pygame.Rect(platform[0], platform[1], platformWidth, platformDepth))
        elif platform[2] == 'bounce':
            pygame.draw.rect(screen, pygame.Color('green'), pygame.Rect(platform[0], platform[1], platformWidth, platformDepth))
    leftPlayer = list(player)
    leftPlayer[0] -= screenWidth
    rightPlayer = list(player)
    rightPlayer[0] += screenWidth
    pygame.draw.rect(screen, pygame.Color('white'), player)
    pygame.draw.rect(screen, pygame.Color('darkgrey'), leftPlayer)
    pygame.draw.rect(screen, pygame.Color('darkgrey'), rightPlayer)
    screen.blit(scoreBoard, scoreBoardRect)
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
                if 'RIGHT' in move:
                    move = 'UPRIGHT'
                elif 'LEFT' in move:
                    move = 'UPLEFT'
                else:
                    move = 'UP'
            if event.key == pygame.K_RIGHT:
                if 'UP' in move:
                    move = 'UPRIGHT'
                else:
                    move = 'RIGHT'
            if event.key == pygame.K_LEFT:
                if 'UP' in move:
                    move = 'UPLEFT'
                else:
                    move = 'LEFT'
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                if 'LEFT' in move:
                    move = 'LEFT'
                if 'RIGHT' in move:
                    move = 'RIGHT'
                else:
                    move = 'STOP'
            if event.key == pygame.K_RIGHT:
                if 'UP' in move:
                    move = 'UP'
                else:
                    move = 'STOP'
            if event.key == pygame.K_LEFT:
                if 'UP' in move:
                    move = 'UP'
                else:
                    move = 'STOP'
    playerInfo, platforms = movePlayer(playerInfo, move, platforms)
    platforms, playerInfo = movePlatforms(platforms)
    playerInfo, platforms, score = moveScreen(playerInfo, platforms, score)
    scoreBoard = font.render(f"Height: {score}", True, pygame.Color('grey'), pygame.Color('black'))
    if playerInfo[1] >= screenHeight + playerSize[1]:
        print("You lost!")
        print("Score:", score)
        break
    printScreen(playerInfo, platforms, scoreBoard, scoreBoardRect)    
    clock.tick(framerate)