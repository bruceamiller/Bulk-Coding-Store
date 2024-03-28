import pygame, sys, math, random

def printScreen():
    screen.fill(pygame.Color('black'))
    pygame.draw.rect(screen, pygame.Color('white'), pygame.Rect(viewPoint[0] - playerSize // 2, viewPoint[1] - playerSize // 2, playerSize, playerSize), 3)
    pygame.draw.line(screen, pygame.Color('white'), viewPoint, lineEndPoint, 3)
    for line in lines:
        pygame.draw.line(screen, pygame.Color('white'), line[0], line[1], 2)
    pygame.display.update()

def detectCollisions(originalEndPoint):
    collisionPoints = []
    for currentLine in lines:
        if abs(currentLine[1][1] - currentLine[0][1]) <= abs(currentLine[1][0] - currentLine[0][0]): #If line is more horizontal than vertical, then we use y-intercept
            currentLine_slope = -(currentLine[1][1] - currentLine[0][1]) / (currentLine[1][0] - currentLine[0][0])
            currentLine_y_int = (currentLine[0][0] * currentLine_slope + (currentLine[0][1]))
            
            x = -(currentLine_y_int - y_intercept) / (slope - currentLine_slope) #What x matches both lines
            y = ((y_intercept * currentLine_slope) - (currentLine_y_int * slope)) / (currentLine_slope - slope) #What y matches both lines  
            
            if ((y <= viewPoint[1] and y >= originalEndPoint[1]) or (y >= viewPoint[1] and y <= originalEndPoint[1])) and (x >= currentLine[0][0] and x <= currentLine[1][0]): #y within view line range(y), and x within wall domain(x)
                collisionPoints.append([x, y])
        elif abs(currentLine[1][1] - currentLine[0][1]) > abs(currentLine[1][0] - currentLine[0][0]):
            slopeX = - 1 / slope
            x_intercept = y_intercept / slope

            currentLine_x_slope = -(currentLine[1][0] - currentLine[0][0]) / (currentLine[1][1] - currentLine[0][1])
            currentLine_x_int = currentLine[1][0] - currentLine_x_slope / currentLine[1][1]

            x = ((x_intercept * currentLine_x_slope) - (currentLine_x_int * slopeX)) / (currentLine_x_slope - slopeX)
            y = (currentLine_x_int - x_intercept) / (slopeX - currentLine_x_slope)

            if ((x <= viewPoint[0] and x >= originalEndPoint[0]) or (x >= viewPoint[0] and x <= originalEndPoint[0])) and (y >= currentLine[0][1] and y <= currentLine[1][1]): 
                collisionPoints.append([x, y])
    if collisionPoints:
        longestDistance = float('inf')
        for point in collisionPoints:
            newDistance = math.dist(viewPoint, point)
            if newDistance < longestDistance:
                closestPoint = point
                longestDistance = newDistance
        return closestPoint
    else:
        return originalEndPoint

def getMaze():
    vrtLines = []
    hrzLines = []
    lines = []
    leftPadding = WIDTH // 16
    rightPadding = WIDTH // 16
    downPadding = WIDTH // 16
    upPadding = WIDTH // 16
    hCells = 10
    vCells = 5
    
    for row in range(vCells + 1):
        for hWall in range(hCells):
            if random.choice([True, False]):
                hrzLines.append([[leftPadding + ((WIDTH - (leftPadding + rightPadding)) / hCells) * hWall, upPadding + ((HEIGHT - (upPadding + downPadding)) / vCells) * row],
                              [leftPadding + ((WIDTH - (leftPadding + rightPadding)) / hCells) * (hWall + 1), upPadding + ((HEIGHT - (upPadding + downPadding)) / vCells) * row]])
    for column in range(hCells + 1):
        for vWall in range(vCells):
            if random.choice([True, False]):
                vrtLines.append([[leftPadding + ((WIDTH - (leftPadding + rightPadding)) / hCells) * column, upPadding + ((HEIGHT - (upPadding + downPadding)) / vCells) * vWall], 
                              [leftPadding + ((WIDTH - (leftPadding + rightPadding)) / hCells) * column, upPadding + ((HEIGHT - (upPadding + downPadding)) / vCells) * (vWall + 1)]])
    lines.extend(vrtLines)
    lines.extend(hrzLines)
    return vrtLines, hrzLines, lines

pygame.init()

framerate = 60
clock = pygame.time.Clock()

rotateSpeed = 5
moveSpeed = 3

HEIGHT = 500
WIDTH = 1000
playerSize = 20

viewPoint = [WIDTH // 2, HEIGHT // 2]
viewAngle = 0
#Line points at origin somewhere far off screen? Why?

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ray Collision')

lineEndPoint = [0, 0]
viewDistance = WIDTH * 2

cornerTouch = 3

#lines = [[[WIDTH // 4, HEIGHT // 4], [WIDTH // 4, HEIGHT * 5 // 12]], [[WIDTH // 4, HEIGHT * 7 // 12], [WIDTH // 4, HEIGHT * 3 // 4]], [[WIDTH * 3 // 4, HEIGHT * 7 // 12], [WIDTH * 3 // 4, HEIGHT * 3 // 4]],
#         [[WIDTH // 4, HEIGHT // 4], [WIDTH * 3 // 4, HEIGHT // 4]], [[WIDTH // 2, HEIGHT * 3 // 4], [WIDTH * 3 // 4, HEIGHT * 3 // 4]], [[WIDTH // 4, HEIGHT // 8], [WIDTH * 3 // 4, HEIGHT // 8]]]
vrtLines, hrzLines, lines = getMaze()

inputs = [(pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_q, pygame.K_e),
          ("moveForward", "moveLeft", "moveBack", "moveRight", "rotateLeft", "rotateRight"),
          [False, False, False, False, False, False]]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            for i, keyName in enumerate(inputs[0]):
                if event.key == keyName:
                    inputs[2][i] = True
        if event.type == pygame.KEYUP:
            for i, keyName in enumerate(inputs[0]):
                if event.key == keyName:
                    inputs[2][i] = False
    
    if inputs[2][inputs[1].index("rotateRight")]:
        viewAngle -= rotateSpeed
    if inputs[2][inputs[1].index("rotateLeft")]:
        viewAngle += rotateSpeed
    if inputs[2][inputs[1].index("moveBack")]:
        viewPoint[0] -= moveSpeed * math.sin(math.radians(viewAngle) + math.pi / 2)
        viewPoint[1] -= moveSpeed * math.cos(math.radians(viewAngle) + math.pi / 2)
    if inputs[2][inputs[1].index("moveForward")]:
        viewPoint[0] += moveSpeed * math.sin(math.radians(viewAngle) + math.pi / 2)
        viewPoint[1] += moveSpeed * math.cos(math.radians(viewAngle) + math.pi / 2)
    if inputs[2][inputs[1].index("moveLeft")]:
        viewPoint[0] -= moveSpeed * math.sin(math.radians(viewAngle))
        viewPoint[1] -= moveSpeed * math.cos(math.radians(viewAngle))
    if inputs[2][inputs[1].index("moveRight")]:
        viewPoint[0] += moveSpeed * math.sin(math.radians(viewAngle))
        viewPoint[1] += moveSpeed * math.cos(math.radians(viewAngle))
    if viewAngle >= 360:
        viewAngle -= 360
    
    lineEndPoint[0] = viewPoint[0] + viewDistance * math.sin(math.radians(viewAngle) + math.pi / 2)
    lineEndPoint[1] = viewPoint[1] + viewDistance * math.cos(math.radians(viewAngle) + math.pi / 2)
    
    try:
        slope = 1 / -math.tan(math.radians(viewAngle) + math.pi / 2)
    except ZeroDivisionError:
        slope = 100000

    for line in vrtLines:
        leftDistance = line[0][0] - viewPoint[0]
        rightDistance = viewPoint[0] - line[0][0]
        if 0 < leftDistance < playerSize // 2 and line[0][1] - playerSize // 2 + cornerTouch  < viewPoint[1] < line[1][1] + playerSize // 2 - cornerTouch:
            viewPoint[0] -= playerSize // 2 - leftDistance
        elif 0 < rightDistance < playerSize // 2 and line[0][1] - playerSize // 2 + cornerTouch < viewPoint[1] < line[1][1] + playerSize // 2 - cornerTouch:
            viewPoint[0] += playerSize // 2 - rightDistance
    for line in hrzLines:
        upDistance = line[0][1] - viewPoint[1]
        downDistance = viewPoint[1] - line[0][1]
        if 0 < upDistance < playerSize // 2 and line[0][0] - playerSize // 2 + cornerTouch < viewPoint[0] < line[1][0] + playerSize // 2 - cornerTouch:
            viewPoint[1] -= playerSize // 2 - upDistance
        elif 0 < downDistance < playerSize // 2 and line[0][0] - playerSize // 2 + cornerTouch < viewPoint[0] < line[1][0] + playerSize // 2 - cornerTouch:
            viewPoint[1] += playerSize // 2 - downDistance

    y_intercept = (viewPoint[0] * slope + viewPoint[1])

    lineEndPoint = detectCollisions(lineEndPoint)

    printScreen()
    clock.tick(framerate)

