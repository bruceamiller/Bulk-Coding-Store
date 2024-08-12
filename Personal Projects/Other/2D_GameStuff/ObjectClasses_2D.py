import math, pygame, random
from CoreMathFunctions_2D import *

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



    """ SETTINGS MANAGEMENT """
    def getPos(self):
        return self._pos
    def setPos(self, newPos):
        for i in range(self._DIMENSIONS):
            self._pos[i] = newPos[i]
    def addPos(self, posChange):
        for i in range(self._DIMENSIONS):
            self._pos[i] += posChange[i]

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

    def __init__(self):
        self._damage = 15
        self._spread = 0.1
        self._burst = 1
        self._range = 85
        self._spreadVariation = 5
        self._timePos = 0
        self._bulletsPerSecond = 4
    
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
    
    def incrementTime(self, timeIncrease):
        self._timePos += timeIncrease

    def shootWeapon(self, entity, targetPos, bulletStore):
        if self._bulletsPerSecond:
            if self._timePos >= FPS / self._bulletsPerSecond:
                self._timePos = 0
                for i in range(self._burst):
                    newBulletPos = list(targetPos)
                    currentBulletSpread = random.random() * self._spread * 2 - self._spread
                    rotateAroundCenter(newBulletPos, entity.getPos(), currentBulletSpread)
                    bullet = entity.getBullet(newBulletPos)
                    bullet.setDamage(self._damage)
                    bullet.setFriction(100 - self._range - random.random() * self._spreadVariation)
                    bulletStore.append(bullet)