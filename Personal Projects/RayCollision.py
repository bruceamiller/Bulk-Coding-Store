import pygame, sys, math, time

def printScreen():
    screen.fill(pygame.Color('black'))
    pygame.draw.circle(screen, pygame.Color('white'), viewPoint, circleSize, 3)
    pygame.draw.line(screen, pygame.Color('white'), viewPoint, lineEndPoint, 3)
    pygame.draw.line(screen, pygame.Color('white'), line1[0], line1[1], 2)
    pygame.display.update()

def detectCollisions(originalEndPoint):
    line1_slope = -(line1[1][1] - line1[0][1]) / (line1[1][0] - line1[0][0])
    line1_y_int = (line1[0][0] * line1_slope + (line1[0][1]))
    try:
        x = -(line1_y_int - y_intercept) / (slope - line1_slope) #What x matches both lines
    except ZeroDivisionError:
        return originalEndPoint
    y = ((y_intercept * line1_slope) - (line1_y_int * slope)) / (line1_slope - slope) #What y matches both lines
    print([x, y], [line1_slope, line1_y_int], [slope, y_intercept], sep="\n", end="\n\n")
    if (y <= viewPoint[1] and y >= originalEndPoint[1]) and (x >= line1[0][0] and x <= line1[1][0]):
        return [x, y]
    else:
        return originalEndPoint

pygame.init()

framerate = 60
clock = pygame.time.Clock()

rotateSpeed = framerate // 60

# Make a centerpoint, with a rotating ray,
# that ends when it has collision with an object.

HEIGHT = 500
WIDTH = 500
circleSize = 10

viewPoint = [WIDTH // 2, HEIGHT // 2]

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ray Collision')

lineEndPoint = [0, 0]
viewDistance = WIDTH * 2

line1 = [[WIDTH // 4, HEIGHT // 4], [WIDTH * 3 // 4, HEIGHT // 8]]
#line1 = [[WIDTH // 4, HEIGHT // 4], [WIDTH // 4, HEIGHT * 3 // 4]]

angle = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    angle += rotateSpeed
    if angle >= 360:
        angle -= 360
    
    lineEndPoint[0] = viewDistance * math.sin(math.radians(angle) + math.pi / 2) + HEIGHT // 2
    lineEndPoint[1] = viewDistance * math.cos(math.radians(angle) + math.pi / 2) + WIDTH // 2
    slope = 1 / -math.tan(math.radians(angle) + math.pi / 2)
    y_intercept = (viewPoint[0] * slope + viewPoint[1])
    viewPoint[0] += 0

    lineEndPoint = detectCollisions(lineEndPoint)

    printScreen()
    clock.tick(framerate)

