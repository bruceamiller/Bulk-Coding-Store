import math, pygame, random
from ObjectClasses_2D import *
from CoreMathFunctions_2D import *

""" USEFUL FUNCTIONS"""
def initializePygame(gameName):
    global SCREEN_WIDTH, SCREEN_HEIGHT, FPS, SCREEN_BUFFER
    SCREEN_WIDTH, SCREEN_HEIGHT = 2500, 1200
    FPS = 60
    SCREEN_BUFFER = 500

    global pygameKeyValues, inputNames, isCurrentInputs
    pygameKeyValues = [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_1, pygame.K_2, pygame.K_3]
    inputNames = ("moveUp", "moveLeft", "moveDown", "moveRight", "equip1", "equip2", "equip3")
    isCurrentInputs = [False for i in range(len(pygameKeyValues))]

    global gameWindow, clock
    gameWindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(gameName)
    clock = pygame.time.Clock()



def isInput(name):
    return isCurrentInputs[inputNames.index(name)]


def drawGame(entities):
    gameWindow.fill(pygame.Color('black'))
    for i in entities:
        i.drawEntity(gameWindow)
    pygame.display.update()

def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            global continueLoop
            continueLoop = False
            return False
        if event.type == pygame.KEYDOWN:
            for i, keyName in enumerate(pygameKeyValues): #For all inputs
                if event.key == keyName:
                    isCurrentInputs[i] = True
        elif event.type == pygame.KEYUP:
            for i, keyName in enumerate(pygameKeyValues): #For all inputs
                if event.key == keyName:
                    isCurrentInputs[i] = False
        global mousePos
        mousePos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            buttonStore = pygame.mouse.get_pressed()
            mouseButtonPressed = None
            if buttonStore.count(True) == 1:
                mouseButtonPressed = buttonStore.index(True)
            if mouseButtonPressed == 0:
                global triggerBullet
                triggerBullet = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if pygame.mouse.get_pressed()[0] == False:
                triggerBullet = False




def getRandomLocation():
    return [random.randrange(-SCREEN_BUFFER, SCREEN_WIDTH + SCREEN_BUFFER)
            , random.randrange(-SCREEN_BUFFER, SCREEN_HEIGHT + SCREEN_BUFFER)]

def getNewMobSpawn(type = None):
    newMobSpawnLoc = getRandomLocation()
    while math.dist(newMobSpawnLoc, player.getPos()) < 500:
        newMobSpawnLoc = getRandomLocation()
    mob = Entity(newMobSpawnLoc, 2)
    if type:
        mob.setColor("blue")
        mob.setHealth(45)
        mob.setMaxVel(1.5)
        mob.setSize(75)
    else:
        mob.setColor("red")
        mob.setSize(40)
    mobStore.append(mob)



initializePygame('2D World Sim')
player = Entity((SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
player.setMoveType("accel")

mobStore = []
playerBulletStore = []
triggerBullet = False

pistol = Weapon()

shotgun = Weapon()
shotgun.setDamage(20)
shotgun.setSpread(150)
shotgun.setBurst(10)
shotgun.setRange(50)
shotgun.setSpreadVariation(10)
shotgun.setBulletsPerSecond(2)

machineGun = Weapon()
machineGun.setDamage(15)
machineGun.setSpread(0.2)
machineGun.setBulletsPerSecond(10)

gunType = "shotgun"
shotGunPellets = 10
shotGunSpread = 150

continueLoop = True
while continueLoop:
    
    drawGame([player] + mobStore + playerBulletStore)
    clock.tick(FPS)

    player.cardinalMove(inputNames, isCurrentInputs)
    for mob in mobStore:
        mob.moveTowards(player.getPos())
    for mob_i in mobStore:
        for mob_j in mobStore:
            if mob_j != mob_i:
                mob_i.separateTouch(mob_j)

    """ WEAPON """
    if isInput("equip1"):
        gunType = "pistol"
    elif isInput("equip2"):
        gunType = "shotgun"
    elif isInput("equip3"):
        gunType = "machineGun"
    if triggerBullet:
        if gunType == "pistol":
            pistol.shootWeapon(player, mousePos, playerBulletStore)
        elif gunType == "shotgun":
            shotgun.shootWeapon(player, mousePos, playerBulletStore)

        elif gunType == "machineGun":
            machineGun.shootWeapon(player, mousePos, playerBulletStore)
    
    for gun in [pistol, shotgun, machineGun]:
        gun.incrementTime(1)


    """ MANAGE BULLETS """
    for bullet in playerBulletStore:
        bullet.updateMove()
        bullet.frictionDeccel()
        bulletVel = bullet.getVel()
        if math.hypot(bulletVel[0], bulletVel[1]) < 5:
            playerBulletStore.remove(bullet)
        for mob in mobStore:
            if bullet.detectBoxCollision(mob):
                mob.damageHealth(bullet.getDamage())
                if mob.getHealth() <= 0:
                    mobStore.remove(mob)
                if bullet in playerBulletStore:
                    playerBulletStore.remove(bullet)

    
    if len(mobStore) < 20:
        if random.random() < 0.2:
            getNewMobSpawn("blue")
        else:
            getNewMobSpawn()

    handleEvents()

    """ Center Player """
    allEntities = [player] + mobStore + playerBulletStore
    shift = player.getDifferenceVector([SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2])
    for entity in allEntities:
        entity.addPos(shift)


    """ LOSE CONDITION """
    for mob in mobStore:
        if player.detectBoxCollision(mob):
            pygame.quit()
            continueLoop = False