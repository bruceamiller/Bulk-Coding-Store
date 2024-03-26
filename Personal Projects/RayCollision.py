import pygame, sys, math, time

def printScreen():
    screen.fill(pygame.Color('black'))
    pygame.draw.circle(screen, pygame.Color('white'), (WIDTH // 2, HEIGHT // 2), circleSize, 3)
    pygame.draw.line(screen, pygame.Color('white'), (WIDTH // 2, HEIGHT // 2), lineEndPoint, 3)
    pygame.draw.line(screen, pygame.Color('white'), line1[0], line1[1], 2)
    pygame.display.update()

def detectCollisions(originalEndPoint):
    line1_slope = (line1[1][1] - line1[0][1]) / (line1[1][0] - line1[0][0])
    line1_y_int = -((line1[0][0] // 2) * line1_slope - (line1[0][1] // 2))
    x = (line1_y_int - y_intercept) / (slope - line1_slope)
    y = 2 * ((y_intercept * line1_slope) - (line1_y_int * slope)) / (line1_slope - slope)
    print(x, y, [line1_slope, line1_y_int])
    if x <= line1[1][0] and x >= line1[0][0] and 0 < angle < 180:
        return [x, y]
    else:
        return originalEndPoint

pygame.init()

framerate = 60
clock = pygame.time.Clock()

rotateSpeed = framerate / 60

# Make a centerpoint, with a rotating ray,
# that ends when it has collision with an object.

HEIGHT = 500
WIDTH = 500
circleSize = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ray Collision')

lineEndPoint = [0, 0]
viewDistance = WIDTH * 2

line1 = [[WIDTH // 4, HEIGHT // 4], [WIDTH * 3 // 4, HEIGHT // 4]]

angle = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    angle += rotateSpeed * math.pi / 180
    
    if angle >= 360:
        angle -= 360
    lineEndPoint[0] = viewDistance * math.sin(angle) + HEIGHT // 2
    lineEndPoint[1] = viewDistance * math.cos(angle) + WIDTH // 2

    slope = math.tan(angle)
    y_intercept = -((WIDTH // 2) * slope - (HEIGHT // 2))

    #Calculate if this line intersects with another line.
    lineEndPoint = detectCollisions(lineEndPoint)

    printScreen()
    clock.tick(framerate)

