import pygame, sys, math, random

def printScreen():
    screen.fill(pygame.Color('black'))
    pygame.draw.circle(screen, pygame.Color('white'), viewPoint, circleSize, 3)
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
    lines = []
    padding = WIDTH // 16
    cells = 5
    #
    for row in range(cells + 1):
        for hWall in range(cells):
            if random.choice([True, False]):
                lines.append([[padding + ((WIDTH - 2 * padding) / cells) * hWall, padding + ((HEIGHT - 2 * padding) / cells) * row], [padding + ((WIDTH - 2 * padding) / cells) * (hWall + 1), padding + ((HEIGHT - 2 * padding) / cells) * row]])
    for column in range(cells + 1):
        for vWall in range(cells):
            if random.choice([True, False]):
                lines.append([[padding + ((WIDTH - 2 * padding) / cells) * column, padding + ((HEIGHT - 2 * padding) / cells) * vWall], [padding + ((WIDTH - 2 * padding) / cells) * column, padding + ((HEIGHT - 2 * padding) / cells) * (vWall + 1)]])
    return lines

pygame.init()

framerate = 60
clock = pygame.time.Clock()

rotateSpeed = 5
moveSpeed = 3

HEIGHT = 500
WIDTH = 500
circleSize = 10

viewPoint = [WIDTH // 2, HEIGHT // 2]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ray Collision')

lineEndPoint = [0, 0]
viewDistance = WIDTH * 2

#lines = [[[WIDTH // 4, HEIGHT // 4], [WIDTH // 4, HEIGHT * 5 // 12]], [[WIDTH // 4, HEIGHT * 7 // 12], [WIDTH // 4, HEIGHT * 3 // 4]], [[WIDTH * 3 // 4, HEIGHT * 7 // 12], [WIDTH * 3 // 4, HEIGHT * 3 // 4]],
#         [[WIDTH // 4, HEIGHT // 4], [WIDTH * 3 // 4, HEIGHT // 4]], [[WIDTH // 2, HEIGHT * 3 // 4], [WIDTH * 3 // 4, HEIGHT * 3 // 4]], [[WIDTH // 4, HEIGHT // 8], [WIDTH * 3 // 4, HEIGHT // 8]]]
lines = getMaze()

inputs = [[pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_q, pygame.K_e],
          ["moveForward", "moveLeft", "moveBack", "moveRight", "rotateLeft", "rotateRight",],
          [False, False, False, False, False, False]]

angle = 0
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
        angle -= rotateSpeed
    if inputs[2][inputs[1].index("rotateLeft")]:
        angle += rotateSpeed
    if inputs[2][inputs[1].index("moveBack")]:
        viewPoint[0] -= moveSpeed * math.sin(math.radians(angle) + math.pi / 2)
        viewPoint[1] -= moveSpeed * math.cos(math.radians(angle) + math.pi / 2)
    if inputs[2][inputs[1].index("moveForward")]:
        viewPoint[0] += moveSpeed * math.sin(math.radians(angle) + math.pi / 2)
        viewPoint[1] += moveSpeed * math.cos(math.radians(angle) + math.pi / 2)
    if inputs[2][inputs[1].index("moveLeft")]:
        viewPoint[0] -= moveSpeed * math.sin(math.radians(angle))
        viewPoint[1] -= moveSpeed * math.cos(math.radians(angle))
    if inputs[2][inputs[1].index("moveRight")]:
        viewPoint[0] += moveSpeed * math.sin(math.radians(angle))
        viewPoint[1] += moveSpeed * math.cos(math.radians(angle))
    if angle >= 360:
        angle -= 360
    
    lineEndPoint[0] = viewDistance * math.sin(math.radians(angle) + math.pi / 2) + HEIGHT // 2
    lineEndPoint[1] = viewDistance * math.cos(math.radians(angle) + math.pi / 2) + WIDTH // 2
    try:
        slope = 1 / -math.tan(math.radians(angle) + math.pi / 2)
    except ZeroDivisionError:
        slope = 10000
    y_intercept = (viewPoint[0] * slope + viewPoint[1])

    lineEndPoint = detectCollisions(lineEndPoint)

    printScreen()
    clock.tick(framerate)

