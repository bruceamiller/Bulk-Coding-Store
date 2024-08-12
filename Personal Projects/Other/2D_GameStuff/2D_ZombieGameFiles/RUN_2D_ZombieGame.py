from pygameUsefulFunctions import *
from ObjectClasses_2D import *
from bulkLoad import *


initializePygame("ZombieGame")


""" GENERAL DATA """
walls, objects = loadMapInfo()
weapons = loadWeapons()

equipped = [weapons[0], weapons[2], None]
for weapon in equipped:
    if weapon:
        weapon.incrementReloadTimer(10000)
currentWeaponPos = 1
mousePos = [0, 0]
activePowerUps = []

hudElements = []
def getWeaponAmmoText():
    return f"{equipped[currentWeaponPos].getAmmoInMag()}/{equipped[currentWeaponPos].getAmmoReserve()}"
weaponAmmo = HudElement("grey", (25, getScreenHeight() - 50), getWeaponAmmoText())
weaponAmmo.setExternalUpdateText(getWeaponAmmoText)
hudElements.append(weaponAmmo)
def getWeaponName():
    return equipped[currentWeaponPos].getName()
weaponName = HudElement("grey", (25, getScreenHeight() - 90), getWeaponName())
weaponName.setExternalUpdateText(getWeaponName)
hudElements.append(weaponName)

def updateHudElements():
    for element in hudElements:
        element.updateText()


def getWeaponHud():
    return getFont().render(f"""{equipped[currentWeaponPos].getName()}/{equipped[currentWeaponPos].getAmmoReserve()}/{equipped[currentWeaponPos].getAmmoInMag()}""", True, pygame.Color("grey"))

def pointsHud():
    return getFont().render(f"""{equipped[currentWeaponPos].getName()}/{equipped[currentWeaponPos].getAmmoReserve()}/{equipped[currentWeaponPos].getAmmoInMag()}""", True, pygame.Color("grey"))


weaponHud = getWeaponHud()
weaponHudRect = weaponHud.get_rect()
weaponHudRect.center = (200, getScreenHeight() - 50)

points = 0



""" ENTITIES """
player = Entity()
player.setMaxVel(4)


playerBulletStore = []

mobStore = []
mobRespawnTimer = Timer()
mobSpawnsPerSecond = 1
mobLimit = 10


""" MAIN FUNCTIONS"""
def handleMovement():
    player.cardinalMove(getInputNames(), getInputStates())

    for bullet in playerBulletStore:
        bullet.updateMove()
        bullet.frictionDeccel()
        if bullet.isStopped() or bullet.touchedWalls(walls):
            playerBulletStore.remove(bullet)
    
    for mob in mobStore:
        mob.moveTowards(player.getPos())

def handleCollision():
    player.wallCollision(walls)
    
    for mob in mobStore:
        mob.wallCollision(walls)
        for bullet in playerBulletStore:
            if bullet.detectBoxCollision(mob):
                            mob.damageHealth(bullet.getDamage())
                            if mob.getHealth() <= 0:
                                mobStore.remove(mob)
                            if bullet in playerBulletStore:
                                playerBulletStore.remove(bullet)
        for otherMob in mobStore:
            if mob != otherMob:
                 mob.separateTouch(otherMob)

clock = getClock()
def incrementTime():
    clock.tick(FPS)
    for weapon in equipped:
        if weapon:
            weapon.incrementTime(1)
            weapon.incrementReloadTimer(1)

    mobRespawnTimer.increment()


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

def handleMobSpawns():
    if len(mobStore) < mobLimit and mobRespawnTimer.getTimeSinceLastReset() > FPS / mobSpawnsPerSecond:
        getNewMobSpawn()
        mobRespawnTimer.reset()

""" MAIN LOOP """
continueLoop = True
while continueLoop:
    drawGame(objects, [player] + playerBulletStore + mobStore, hudElements)
    
    incrementTime()

    handleMovement()
    handleCollision()
    centerAround(player, objects + [player] + playerBulletStore + mobStore)

    """ HANDLE INTERACTION """
    #Shoot Weapon
    if weaponTriggered():
        equipped[currentWeaponPos].handleShooting(player, mousePos, playerBulletStore)
    #Choose equipped weapon
    if isInput("equip1"):
        currentWeaponPos = 0
    elif isInput("equip2"):
        currentWeaponPos = 1
    elif "thirdGun" in activePowerUps and isInput("equip3"):
        currentWeaponPos = 2
    if isInput("reload"):
        equipped[currentWeaponPos].reload()
    updateHudElements()
    
    handleMobSpawns()

    continueLoop = handleEvents(mousePos)

    for mob in mobStore:
        if mob.detectBoxCollision(player):
            pygame.quit()
            continueLoop = False
    
