import pygame, random, math

pygame.init()

# Draw a  constantly updating sparkler using code...
# Have large sparks form and break randomly into smaller sparks.
# Sparks leave trails behind them, thinner where it starts and thicker near each spark.

def rotateAroundCenter(objectPos, centerPos, angle):
    vectorFromCenter = [0.0, 0.0]
    for i in range(2):
        vectorFromCenter[i] = centerPos[i] - objectPos[i]
    rotatedVector = [0.0, 0.0]
    rotatedVector[0] = vectorFromCenter[0] * math.cos(angle) - vectorFromCenter[1] * math.sin(angle)
    rotatedVector[1] = vectorFromCenter[0] * math.sin(angle) + vectorFromCenter[1] * math.cos(angle)
    for i in range(2):
        objectPos[i] += rotatedVector[i] - vectorFromCenter[i]
    return rotatedVector

class Spark():

    def __init__(self, posx, posy, size, velx = 0, vely = 0):
        self._posx = posx
        self._posy = posy
        self._velx = velx
        self._vely = vely
        self._size = size

    def explodedSmallerSparks(self):
        #subSparksAmount = random.randrange(1, int(self._size))
        subSparksAmount = random.randrange(1, 10)
        subSparkSize = math.sqrt(self._size / subSparksAmount * 3)
        self._size = 0
        subSparks = []

        for spark in range(0, subSparksAmount):
            #Exponential (Creates more smaller Sparks)
            explosionDistance = (random.random() ** 10) * (explosionSpeedMax - explosionSpeedMin) + explosionSpeedMin
            #Linear (Creates equal of all spark range)
            #explosionDistance = random.randrange(explosionSpeedMin, explosionSpeedMax)
            explosionPos = [self._posx + explosionDistance, self._posy]
            explosionPos = rotateAroundCenter(explosionPos, [self._posx, self._posy], random.randrange(0, 360))
            newSpark = Spark(self._posx, self._posy, subSparkSize, explosionPos[0], explosionPos[1])

            subSparks.append(newSpark)

        # make subSparks, reduce size of center spark

        return subSparks
    
    def getSize(self):
        return self._size

    def reduceSize(self, reduction):
        self._size -= reduction

    def drawSmoke(self):
        pygame.draw.circle(screen, pygame.Color("grey15"), (self._posx, self._posy), self._size * 5)

    def drawSpark(self):
        # Take spark pos, vel & size -> draw spark trails

        #brightColor = (238, 232, 170)
        brightColor = (255, 255, 255)
        darkColor = (160, 82, 45)
        colorDifference = tuple(brightColor[i] - darkColor[i] for i in range(3))
        currentSparkColor = tuple(darkColor[i] + colorDifference[i] / largeSparkSize * self._size for i in range(3))

        pygame.draw.circle(screen, pygame.Color(currentSparkColor), (self._posx, self._posy), self._size)
    
    def drawTrail(self):
        brightColor = (238, 232, 170)
        darkColor = (160, 82, 45)
        colorDifference = tuple(brightColor[i] - darkColor[i] for i in range(3))
        currentSparkColor = tuple(darkColor[i] + colorDifference[i] / largeSparkSize * self._size for i in range(3))

        pygame.draw.line(screen, currentSparkColor, (self._posx, self._posy), (self._posx - self._velx / framerate * 2, self._posy - self._vely / framerate * 2), int(self._size))

    def update(self):
        gravity = 10

        self._vely += gravity

        self._posx += self._velx / framerate
        self._posy += self._vely / framerate

        #update spark movement & size
        #explode spark if what? random time?

        pass



screenWidth, screenHeight = 1200, 800
screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.RESIZABLE)
pygame.display.set_caption('Sparkler Sim')

clock = pygame.time.Clock()
framerate = 60

sparkSourceX, sparkSourceY = screenWidth // 2, screenHeight // 2
airResistance = 1
smallestSparkSize = 0.01
largeSparkSize = 10
explosionSpeedMin = 400
explosionSpeedMax =  600

explodeChance = 0.1

shrinkSpeed = 0.1


sparkStore = []

pygame.mouse.set_visible(False)

continueSparkling = True
while continueSparkling:
    sparkSourceX, sparkSourceY = pygame.mouse.get_pos()

    #Continue drawing source spark
    newSourceSpark = Spark(sparkSourceX, sparkSourceY, largeSparkSize)


    #Draw sparks
    screen.fill(pygame.Color('black'))
    for spark in sparkStore:
        spark.reduceSize(shrinkSpeed)
        spark.update()

    for spark in sparkStore:
        spark.drawSmoke()
    newSourceSpark.drawSmoke()
    
    for spark in sparkStore:
        spark.drawSpark()
    
    for spark in sparkStore:
        spark.drawTrail()
    newSourceSpark.drawSpark()

    sparkStore.extend(newSourceSpark.explodedSmallerSparks())
    
    for spark in sparkStore:
        if spark.getSize() < smallestSparkSize:
            sparkStore.remove(spark)
    pygame.display.update()


    for spark in sparkStore:
        if spark.getSize() >= 2 and random.random() < explodeChance:
            sparkStore.extend(spark.explodedSmallerSparks())

    clock.tick(framerate)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                continueSparkling = False
