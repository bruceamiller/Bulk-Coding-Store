import math, pygame, random
from CoreMathFunctions_2D import *
from pygameUsefulFunctions import *

FPS = 60

class Entity():
    
    def __init__(self, startPos = [0.0, 0.0], maxVel = 5):
        self._pos = [0.0, 0.0]
        for i in range(len(self._pos)):
            self._pos[i] = startPos[i]

        self._vel = [0.0, 0.0]
        self._accel = [0.0, 0.0]

        self._maxVel = maxVel
        self._accelSpeed = 75
        self._friction = 50

        self._size = 50
        self._color = "white"
        self._name = "Entity"

        self._DIMENSIONS = 2

        self._movementType = "vel"

        self._health = 10
        self._damage = 5

        self._score = 0



    """ SETTINGS MANAGEMENT """
    def getPos(self):
        return self._pos
    def setPos(self, newPos):
        for i in range(self._DIMENSIONS):
            self._pos[i] = newPos[i]
    def addPos(self, posChange):
        for i in range(self._DIMENSIONS):
            self._pos[i] += posChange[i]
    
    def setScore(self, newScore):
        self._score = newScore
    
    def addScore(self, pointsAdded):
        self._score += pointsAdded
    
    def buyWithPoints(self, pointCost):
        if self._score - pointCost >= 0:
            self._score -= pointCost
            return True
        else:
            return False


    def getVel(self):
        return self._vel
    def setVel(self, newVel):
        for i in range(self._DIMENSIONS):
            self._vel[i] = newVel[i]
    def addVel(self, velChange):
        for i in range(self._DIMENSIONS):
            self._vel[i] += velChange[i]
        if math.hypot(self._vel[0], self._vel[1]) > self._maxVel:
            self._vel = newLengthVector(self._vel, self._maxVel)

    def setMaxVel(self, newMaxVel):
        self._maxVel = newMaxVel

    def getAccel(self):
        return self._accel
    def setAccel(self, newAccel):
        for i in range(self._DIMENSIONS):
            self._accel[i] = newAccel[i]
    def addAccel(self, accelChange):
        for i in range(self._DIMENSIONS):
            self._accel[i] += accelChange[i]

    def getFriction(self):
        return self._friction
    def setFriction(self, newFriction):
        self._friction = newFriction
    
    def getSize(self):
        return self._size
    def setSize(self, newSize):
        self._size = newSize
    
    def getColor(self):
        return self._color
    def setColor(self, newColor):
        self._color = newColor
    
    def setMoveType(self, newType):
        self._movementType = newType
    
    def getHealth(self):
        return self._health
    def setHealth(self, newHealth):
        self._health = newHealth
    def damageHealth(self, damage):
        self._health -= damage
    
    def getDamage(self):
        return self._damage
    def setDamage(self, newDamage):
        self._damage = newDamage

    """ MOVEMENT TOOLS """
    def updateMove(self):
        self.addVel(self._accel)
        self.addPos(self._vel)

    def frictionDeccel(self):
        if math.hypot(self._vel[0], self._vel[1]) > math.hypot(self._friction / FPS, self._friction / FPS):
            self.addVel(newLengthVector(self._vel, -self._friction / FPS))
        else:
            self._vel = [0.0, 0.0]
    
    def cardinalMove(self, inputNames, isCurrentInputs):
        def isInput(name):
            return isCurrentInputs[inputNames.index(name)]
        if self._movementType == "vel":
            if isInput("moveLeft"):
                self.addPos((-self._maxVel, 0))
            if isInput("moveRight"):
                self.addPos((self._maxVel, 0))
            if isInput("moveUp"):
                self.addPos((0, -self._maxVel))
            if isInput("moveDown"):
                self.addPos((0, self._maxVel))
        elif self._movementType == "accel":
            if isInput("moveLeft") and not isInput("moveRight"):
                self.addVel((-self._accelSpeed / FPS, 0))
            elif isInput("moveRight") and not isInput("moveLeft"):
                self.addVel((self._accelSpeed / FPS, 0))
            if isInput("moveUp") and not isInput("moveDown"):
                self.addVel((0, -self._accelSpeed / FPS))
            elif isInput("moveDown") and not isInput("moveUp"):
                self.addVel((0, self._accelSpeed / FPS))
        self.updateMove()
        self.frictionDeccel()

    def moveTowards(self, pos):
        differenceVector = self.getDifferenceVector(pos)
        if self._movementType == "vel":
            self.addVel(newLengthVector(differenceVector, self._maxVel))
        self.updateMove()
    
    def isStopped(self):
        vel = self.getVel()
        if math.hypot(vel[0], vel[1]) < 10:
            return True
        return False



    """ COLLISION MANAGEMENT """
    def detectBoxCollision(self, otherEntity):
        otherMobPos = otherEntity.getPos()
        otherMobSize = otherEntity.getSize()
        if math.dist([self._pos[0]], [otherMobPos[0]]) < self._size / 2 + otherMobSize / 2 and math.dist([self._pos[1]], [otherMobPos[1]]) < self._size / 2 + otherMobSize / 2:
            return True
        return False

    def separateTouch(self, otherMob):
        sharedDistance = self._size / 2 + otherMob.getSize() / 2
        if self.detectBoxCollision(otherMob):
            differenceVector = self.getDifferenceVector(otherMob.getPos())
            shiftPos = [0.0, 0.0]
            for i in range(self._DIMENSIONS):
                if differenceVector[i] > 0 and differenceVector[i] < sharedDistance:
                    shiftPos[i] += (differenceVector[i] - sharedDistance)
                elif differenceVector[i] < 0 and differenceVector[i] > -sharedDistance:
                    shiftPos[i] += (differenceVector[i] + sharedDistance)
            if differenceVector[0] < differenceVector[1]:
                self.addVel([0.0, shiftPos[1]])
            else:
                self.addVel([shiftPos[0], 0.0])
    
    def wallCollision(self, walls):
        for wall in walls:
            wallPos = wall.getPos()
            wallWidth = wall.getWidth()
            wallHeight = wall.getHeight()
            horizontalOffset = self._pos[0] - wallPos[0]
            verticalOffset = self._pos[1] - wallPos[1]
            horizontalTouchBuffer = wallWidth / 2 + self._size / 2
            verticalTouchBuffer = wallHeight / 2 + self._size / 2
            if abs(horizontalOffset) < horizontalTouchBuffer and abs(verticalOffset) < verticalTouchBuffer:
                if abs(horizontalTouchBuffer) - abs(horizontalOffset) <= abs(verticalTouchBuffer) - abs(verticalOffset):
                    if horizontalOffset > 0:
                        self.addPos((horizontalTouchBuffer - horizontalOffset, 0))
                    elif horizontalOffset < 0:
                        self.addPos((-horizontalTouchBuffer - horizontalOffset, 0))
                else:
                    if verticalOffset > 0:
                        self.addPos((0, verticalTouchBuffer - verticalOffset, 0))
                    elif verticalOffset < 0:
                        self.addPos((0, -verticalTouchBuffer - verticalOffset))
    
    def touchedWalls(self, walls):
        for wall in walls:
            wallPos, wallWidth, wallHeight = wall.getPos(), wall.getWidth(), wall.getHeight()
            horizontalOffset, verticalOffset = self._pos[0] - wallPos[0], self._pos[1] - wallPos[1]
            horizontalTouchBuffer = wallWidth / 2 + self._size / 2
            verticalTouchBuffer = wallHeight / 2 + self._size / 2
            if abs(horizontalOffset) < horizontalTouchBuffer and abs(verticalOffset) < verticalTouchBuffer:
                return True


    """ UTILITY """
    def drawEntity(self, gameWindow):
        pygame.draw.rect(gameWindow, pygame.Color(self._color)
        , pygame.Rect(self._pos[0] - self._size // 2, self._pos[1] - self._size // 2, self._size, self._size))
       
    def getDifferenceVector(self, pos):
        differenceVector = [0.0, 0.0]
        for i in range(self._DIMENSIONS):
            differenceVector[i] = pos[i] - self._pos[i]
        return differenceVector


    """ ENTITY SPECIFIC """
    def getBullet(self, targetPos, speed = 20):
        BULLET_SIZE = 10
        BULLET_MAX_SPEED = speed
        bullet = Entity(self.getPos(), BULLET_MAX_SPEED)
        bullet.setSize(BULLET_SIZE)
        differenceVector = self.getDifferenceVector(targetPos)
        bullet.setVel(newLengthVector(differenceVector, BULLET_MAX_SPEED))
        return bullet

class Weapon():

    def __init__(self, name):
        self._name = name
        
        self._damage = 15
        self._spread = 0.1
        self._burst = 1
        self._range = 85
        self._spreadVariation = 5
        self._timePos = 0
        self._bulletsPerSecond = 4

        self._maxAmmo = 120
        self._magSize = 15
        self._ammoReserve = self._maxAmmo - self._magSize
        self._ammoInMag = self._magSize

        self._semiAuto = True

        self._reloadTimer = Timer()
        self._reloadSpeed = 1

    def getName(self):
        return self._name
    
    def getAmmoInMag(self):
        return self._ammoInMag

    def getAmmoReserve(self):
        return self._ammoReserve
    
    def setDamage(self, newDamage):
        self._damage = newDamage
    
    def setSpread(self, newSpread):
        self._spread = newSpread
    
    def setBurst(self, newBurst):
        self._burst = newBurst
    
    def setRange(self, newRange):
        self._range = newRange
    
    def setSpreadVariation(self, newVariation):
        self._spreadVariation = newVariation
    
    def setBulletsPerSecond(self, newBulletsPerSecond):
        self._bulletsPerSecond = newBulletsPerSecond

    def setSemiAuto(self, semiAuto):
        self._semiAuto = semiAuto
    
    def setMagSize(self, newMagSize):
        self._magSize = newMagSize
        self._ammoInMag = newMagSize
    
    def setMaxAmmo(self, newReserveSize):
        self._maxAmmo = newReserveSize
        self._ammoReserve = self._maxAmmo - self._magSize
    
    def setReloadSpeed(self, newReloadSpeed):
        self._reloadSpeed = newReloadSpeed

    """ WEAPON INTERACTION """

    def incrementTime(self, timeIncrease):
        self._timePos += timeIncrease

    def handleShooting(self, entity, targetPos, bulletStore):
        if self._bulletsPerSecond and self._ammoInMag > 0 and self._reloadTimer.getTimeSinceLastReset() > self._reloadSpeed * FPS:
            if self._timePos >= FPS / self._bulletsPerSecond:
                if self._semiAuto:
                    setWeaponTriggered(False)
                self._timePos = 0
                for i in range(self._burst):
                    newBulletPos = list(targetPos)
                    currentBulletSpread = random.random() * self._spread * 2 - self._spread
                    rotateAroundCenter(newBulletPos, entity.getPos(), currentBulletSpread)
                    bullet = entity.getBullet(newBulletPos)
                    bullet.setDamage(self._damage)
                    bullet.setFriction(100 - self._range - random.random() * self._spreadVariation)
                    bulletStore.append(bullet)
                    self._ammoInMag -= 1

    def reload(self):
        if self._ammoInMag < self._magSize and self._reloadTimer.getTimeSinceLastReset() > self._reloadSpeed * FPS:
            neededAmmo = self._magSize - self._ammoInMag
            if self._ammoReserve >= neededAmmo:
                self._ammoReserve -= neededAmmo
                self._ammoInMag = self._magSize # += neededAmmo
            elif self._ammoReserve > 1:
                self._ammoInMag += self._ammoReserve
                self._ammoReserve = 0
            self._reloadTimer.reset()
    
    def incrementReloadTimer(self, time = 1):
        self._reloadTimer.increment(1)




class Floor():

    def __init__(self, pos1, pos2, color = "grey"):
        self._pos1 = pos1
        self._pos2 = pos2
        self._color = color
        self._image = None
    
    def addPos(self, posChange):
        for i in range(2):
            self._pos1[i] += posChange[i]
            self._pos2[i] += posChange[i]

    def setImage(self, image):
        self._image = image

    def drawObject(self, gameWindow):
        if self._image:
            pygame.Surface.blit(gameWindow, self._image, self._pos1)
        else:
            pygame.draw.rect(gameWindow, pygame.Color(self._color)
            , pygame.Rect(self._pos1[0], self._pos1[1], self._pos2[0] - self._pos1[0], self._pos2[1] - self._pos1[1]))

class Wall():
    def __init__(self, pos, width = 15, height = 15):
        self._pos = pos
        self._width = width
        self._height = height
        #self._color = "black"
        self._color = (55, 72, 62)
    
    def getPos(self):
        return self._pos
    
    def getWidth(self):
        return self._width

    def getHeight(self):
        return self._height
    
    def setColor(self, newColor):
        self._color = newColor

    def drawObject(self, gameWindow):
        if self._color:
            pygame.draw.rect(gameWindow, pygame.Color(self._color), 
                            pygame.Rect(self._pos[0] - self._width / 2, self._pos[1] - self._height / 2, self._width, self._height))
    
    def addPos(self, posChange):
        for i in range(2):
            self._pos[i] += posChange[i]

class Timer():
    def __init__(self):
        self._timeSinceLastReset = 0
    
    def increment(self, increment = 1):
        self._timeSinceLastReset += increment
    
    def reset(self):
        self._timeSinceLastReset = 0
    
    def getTimeSinceLastReset(self):
        return self._timeSinceLastReset

class HudElement():
    def __init__(self, color, screenPos = [0, 0], text = "blank"):
        self._screenPos = screenPos
        self._color = color
        self._hudText = getFont().render(text, True, pygame.Color(self._color))
        self._hudRect = self._hudText.get_rect()
        self._hudRect.topleft = screenPos
        self._updateTextFunc = None
    
    def updateText(self, text):
        self._hudText = text

    def setExternalUpdateText(self, newFunc):
        self._updateTextFunc = newFunc

    def updateText(self):
        self._hudText = getFont().render(self._updateTextFunc(), True, pygame.Color(self._color))
    
    def drawElement(self, gameWindow):
        gameWindow.blit(self._hudText, self._hudRect)