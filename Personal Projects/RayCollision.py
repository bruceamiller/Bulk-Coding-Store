import pygame, sys, math, random

HEIGHT = 1000
WIDTH = 2000

def printScreen():
    screen.fill(pygame.Color('black'))
    pygame.draw.rect(screen, pygame.Color((15, 15, 15)), pygame.Rect(0, 0, WIDTH, HEIGHT // 2))
    for w in walls:
        pygame.draw.rect(screen, pygame.Color((w[1], w[1], w[1])), w[0])
    pygame.draw.rect(screen, pygame.Color('white'), pygame.Rect(viewPoint[0] - playerSize // 2, viewPoint[1] - playerSize // 2, playerSize, playerSize), 3)
    for r in rays:
        pygame.draw.line(screen, pygame.Color('white'), viewPoint, r[:2], 3)
    for line in lines:
        pygame.draw.line(screen, pygame.Color('white'), line[0], line[1], 2)
    pygame.display.update()


def detectCollisions(currentLineEndPt, slope, y_intercept):
    collisionPoints = []
    for currentLine in lines:
        if abs(currentLine[1][1] - currentLine[0][1]) <= abs(currentLine[1][0] - currentLine[0][0]): #If line is more horizontal than vertical, then we use y-intercept
            currentLine_slope = -(currentLine[1][1] - currentLine[0][1]) / (currentLine[1][0] - currentLine[0][0])
            currentLine_y_int = (currentLine[0][0] * currentLine_slope + (currentLine[0][1]))
            
            x = -(currentLine_y_int - y_intercept) / (slope - currentLine_slope) #What x matches both lines
            y = ((y_intercept * currentLine_slope) - (currentLine_y_int * slope)) / (currentLine_slope - slope) #What y matches both lines  
            
            if ((y <= viewPoint[1] and y >= currentLineEndPt[1]) or (y >= viewPoint[1] and y <= currentLineEndPt[1])) and (x >= currentLine[0][0] and x <= currentLine[1][0]): #y within view line range(y), and x within wall domain(x)
                collisionPoints.append([x, y])
        elif abs(currentLine[1][1] - currentLine[0][1]) > abs(currentLine[1][0] - currentLine[0][0]):
            slopeX = - 1 / slope
            x_intercept = y_intercept / slope

            currentLine_x_slope = -(currentLine[1][0] - currentLine[0][0]) / (currentLine[1][1] - currentLine[0][1])
            currentLine_x_int = currentLine[1][0] - currentLine_x_slope / currentLine[1][1]

            x = ((x_intercept * currentLine_x_slope) - (currentLine_x_int * slopeX)) / (currentLine_x_slope - slopeX)
            y = (currentLine_x_int - x_intercept) / (slopeX - currentLine_x_slope)

            if ((x <= viewPoint[0] and x >= currentLineEndPt[0]) or (x >= viewPoint[0] and x <= currentLineEndPt[0])) and (y >= currentLine[0][1] and y <= currentLine[1][1]): 
                collisionPoints.append([x, y])
    if collisionPoints:
        shortestDistance = float('inf')
        for point in collisionPoints:
            newDistance = math.dist(viewPoint, point)
            if newDistance < shortestDistance:
                closestPoint = point
                shortestDistance = newDistance
        return closestPoint, shortestDistance
    else:
        return currentLineEndPt, viewDistance


def getMaze():
    vrtLines = []
    hrzLines = []
    lines = []
    leftPadding = WIDTH // 16
    rightPadding = WIDTH // 16
    downPadding = WIDTH // 16
    upPadding = WIDTH // 16
    hCells = 20
    vCells = 10
    
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


inputs = [(pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_q, pygame.K_e, pygame.K_LCTRL),
          ("moveForward", "moveLeft", "moveBack", "moveRight", "rotateLeft", "rotateRight", "run"),
          [False, False, False, False, False, False, False]]

def getInputs():
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
pygame.init()

viewAngle = 0
rotateSpeed = 5

def rotateView(angle):
    if inputs[2][inputs[1].index("rotateRight")]:
        angle -= rotateSpeed
    if inputs[2][inputs[1].index("rotateLeft")]:
        angle += rotateSpeed
    if angle >= 360:
        angle -= 360
    return angle

def getEndPoint(angle):
    endPoint = [0, 0]
    endPoint[0] = viewPoint[0] + viewDistance * math.sin(math.radians(angle) + math.pi / 2)
    endPoint[1] = viewPoint[1] + viewDistance * math.cos(math.radians(angle) + math.pi / 2)
    return endPoint

moveSpeed = [0, 2, 5] # [currentMoveSpeed, walkSpeed, runSpeed]
moveSpeed[0] = moveSpeed[1]

viewPoint = [WIDTH // 2, HEIGHT // 2]

def movePlayer(viewAngle):
    if inputs[2][inputs[1].index("run")]:
        moveSpeed[0] = moveSpeed[2]
    else:
        moveSpeed[0] = moveSpeed[1]
    
    if inputs[2][inputs[1].index("moveBack")]:
        viewPoint[0] -= moveSpeed[0] * math.sin(math.radians(viewAngle) + math.pi / 2)
        viewPoint[1] -= moveSpeed[0] * math.cos(math.radians(viewAngle) + math.pi / 2)
    if inputs[2][inputs[1].index("moveForward")]:
        viewPoint[0] += moveSpeed[0] * math.sin(math.radians(viewAngle) + math.pi / 2)
        viewPoint[1] += moveSpeed[0] * math.cos(math.radians(viewAngle) + math.pi / 2)
    if inputs[2][inputs[1].index("moveLeft")]:
        viewPoint[0] -= moveSpeed[0] * math.sin(math.radians(viewAngle))
        viewPoint[1] -= moveSpeed[0] * math.cos(math.radians(viewAngle))
    if inputs[2][inputs[1].index("moveRight")]:
        viewPoint[0] += moveSpeed[0] * math.sin(math.radians(viewAngle))
        viewPoint[1] += moveSpeed[0] * math.cos(math.radians(viewAngle))

    lineEndPoint[:2] = getEndPoint(viewAngle)

def getSlope(angle):
    #
    # Takes angle, returns slope of line
    #
    try:
        slope = -1 / math.tan(math.radians(angle) + math.pi / 2)
    except ZeroDivisionError:
        slope = 10000
    return slope

def getY_Intercept(slope):
    y_intercept = (viewPoint[0] * slope + viewPoint[1])
    return y_intercept

FOV = 120
rayNum = 60
lineEndPoint = [0, 0]
rays = []
for r in range(rayNum): #Ray: [endpoint_x endpoint_y, angle, rayDistance]
    rayAngle = (FOV / (rayNum - 1)) * (r) + viewAngle - FOV // 2
    rays.append([0, 0, rayAngle, 255])

def getWalls():
    walls = []
    for i, r in enumerate(rays):
        wallDepth = 255 - 255 * (r[3] / viewDistance)

        wallWidth = WIDTH // rayNum
        wallHeight = HEIGHT * ((wallDepth) / 255)
        
        wallLeft = wallWidth * (rayNum - i)
        wallTop = (HEIGHT - wallHeight) / 2

        
        wallRect = [pygame.Rect(wallLeft, wallTop, wallWidth, wallHeight), wallDepth]
        walls.append(wallRect)
        print(wallDepth)
    
    return walls

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ray Collision')


viewDistance = 1000
wallColor = 255 # for graphics





playerSize = 20
framerate = 60
clock = pygame.time.Clock()

vrtLines, hrzLines, lines = getMaze()

while True:
    getInputs()
    
    viewAngle = rotateView(viewAngle)
    movePlayer(viewAngle)


    for r in rays:
        r[2] = rotateView(r[2])
        r[:2] = getEndPoint(r[2])

        raySlope = getSlope(r[2])
        rayIntercept = getY_Intercept(raySlope)
        rayOrigEndPt = r[:2]
        r[:2], r[3] = detectCollisions(rayOrigEndPt, raySlope, rayIntercept)
        r[:2],
    
    #Collision w/ player
    for line in vrtLines:
        leftDistance = line[0][0] - viewPoint[0]
        rightDistance = viewPoint[0] - line[0][0]
        if 0 < leftDistance < playerSize // 2 and line[0][1] - playerSize // 2 + moveSpeed[0] + 1  < viewPoint[1] < line[1][1] + playerSize // 2 - moveSpeed[0] - 1:
            viewPoint[0] -= playerSize // 2 - leftDistance
        elif 0 < rightDistance < playerSize // 2 and line[0][1] - playerSize // 2 + moveSpeed[0] + 1 < viewPoint[1] < line[1][1] + playerSize // 2 - moveSpeed[0] - 1:
            viewPoint[0] += playerSize // 2 - rightDistance
    for line in hrzLines:
        upDistance = line[0][1] - viewPoint[1]
        downDistance = viewPoint[1] - line[0][1]
        if 0 < upDistance < playerSize // 2 and line[0][0] - playerSize // 2 + moveSpeed[0] + 1 < viewPoint[0] < line[1][0] + playerSize // 2 - moveSpeed[0] - 1:
            viewPoint[1] -= playerSize // 2 - upDistance
        elif 0 < downDistance < playerSize // 2 and line[0][0] - playerSize // 2 + moveSpeed[0] + 1 < viewPoint[0] < line[1][0] + playerSize // 2 - moveSpeed[0] - 1:
            viewPoint[1] += playerSize // 2 - downDistance

    walls = getWalls()

    printScreen()
    clock.tick(framerate)
