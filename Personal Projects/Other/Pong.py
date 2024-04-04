import pygame, sys, random

pygame.init()



framerate = 60
speed = framerate // 10
clock = pygame.time.Clock()

screenHeight = 750
screenWidth = screenHeight * 2
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Pong')



paddleWidth = screenHeight // 50
paddleHeight = screenHeight // 6
ballSize = screenHeight / 50
wallBuffer = int(screenHeight // 7.5)

paddleInfo1 = [wallBuffer, screenHeight // 2 - (paddleHeight // 2), 0] #x, y, score
paddleInfo2 = [screenWidth - wallBuffer - paddleWidth, screenHeight // 2 - (paddleHeight // 2), 0]
paddleDirection = 'STOP'

font = pygame.font.Font('freesansbold.ttf', 32)
scoreBoard = font.render(f"{paddleInfo1[2]}    {paddleInfo2[2]}", True, pygame.Color('white'), pygame.Color('black'))
scoreBoardRect = scoreBoard.get_rect()
scoreBoardRect.center = (screenWidth // 2, wallBuffer // 4)

def ballMake():
    return [screenWidth // 2, screenHeight // 2 + random.randint(-300, 300), random.choice(['UpRight', 'UpLeft', 'DownRight', 'DownLeft'])] # x, y, direction

ballInfo = ballMake()

def paddleMove(paddleInfo, paddleDirection):
    if paddleDirection == 'UP' and paddleInfo[1] >= 0:
        paddleInfo[1] -= speed / 2
    if paddleDirection == 'DOWN' and paddleInfo[1] <= screenHeight - paddleHeight:
        paddleInfo[1] += speed / 2
    return paddleInfo

def paddleComputer(paddleInfo, ballInfo):
    if paddleInfo[1] > ballInfo[1]:
        paddleDirection = 'UP'
    if paddleInfo[1] < ballInfo[1]:
        paddleDirection = 'DOWN'
    else:
        paddleDirection = 'UP'
    return paddleDirection

def ballMove(paddleInfo1, paddleInfo2, ballInfo):
    if 'Up' in ballInfo[2]:
        ballInfo[1] -= speed
    if 'Down' in ballInfo[2]:
        ballInfo[1] += speed
    if 'Left' in ballInfo[2]:
        ballInfo[0] -= speed
    if 'Right' in ballInfo[2]:
        ballInfo[0] += speed
    if  -1 > ballInfo[1]:
        ballInfo[1] += speed
        ballInfo[2] = ballInfo[2].replace("Up", "Down")
    elif screenHeight - ballSize < ballInfo[1]:
        ballInfo[1] -= speed
        ballInfo[2] = ballInfo[2].replace("Down", "Up")
    if wallBuffer + paddleWidth > ballInfo[0] > wallBuffer and paddleInfo1[1] < ballInfo[1] < paddleInfo1[1] + paddleHeight:
        ballInfo[0] += speed
        ballInfo[2] = ballInfo[2].replace("Left", "Right")
    elif screenWidth - wallBuffer - paddleWidth - ballSize < ballInfo[0] < screenWidth - wallBuffer and paddleInfo2[1] < ballInfo[1] < paddleInfo2[1] + paddleHeight:
        ballInfo[0] -= speed
        ballInfo[2] = ballInfo[2].replace("Right", "Left")
    return ballInfo

def winCheck(ballInfo):
    if 0 > ballInfo[0]:
        return (0, 1), ballMake()
    elif ballInfo[0] > screenWidth-ballSize:
        return (1, 0), ballMake()
    else:
        return (0, 0), ballInfo

def printScreen(paddleInfo1, paddleInfo2, ballInfo, scoreBoard, scoreBoardRect):
    screen.fill(pygame.Color('black'))
    screen.blit(scoreBoard, scoreBoardRect)
    pygame.draw.rect(screen, pygame.Color('grey'), pygame.Rect(screenWidth // 2, 0, 1, screenHeight))
    pygame.draw.rect(screen, pygame.Color('white'), pygame.Rect(paddleInfo1[0], paddleInfo1[1], paddleWidth, paddleHeight))
    pygame.draw.rect(screen, pygame.Color('white'), pygame.Rect(paddleInfo2[0], paddleInfo2[1], paddleWidth, paddleHeight))
    pygame.draw.rect(screen, pygame.Color('white'), pygame.Rect(ballInfo[0], ballInfo[1], ballSize, ballSize))
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
                paddleDirection = 'UP'
            if event.key == pygame.K_DOWN:
                paddleDirection = 'DOWN'
        if event.type == pygame.KEYUP:
            paddleDirection = 'STOP'
    paddleInfo1 = paddleMove(paddleInfo1, paddleDirection)

    computerPaddleDirection = paddleComputer(paddleInfo2, ballInfo)
    paddleInfo2 = paddleMove(paddleInfo2, computerPaddleDirection)

    ballInfo = ballMove(paddleInfo1, paddleInfo2, ballInfo)
    scored, ballInfo = winCheck(ballInfo)
    if 1 in scored:
        paddleInfo1[2] += scored[0]
        paddleInfo2[2] += scored[1]
        print([paddleInfo1[2], paddleInfo2[2]])
        scoreBoard = font.render(f"{paddleInfo1[2]}    {paddleInfo2[2]}", True, pygame.Color('white'), pygame.Color('black'))
    printScreen(paddleInfo1, paddleInfo2, ballInfo, scoreBoard, scoreBoardRect)
    if paddleInfo1[2] >= 10:
        print("Player Wins!")
        break
    elif paddleInfo2[2] >= 10:
        print("Computer Wins.")
        break
    clock.tick(framerate)
