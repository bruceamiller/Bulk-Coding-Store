import pygame, random

def initializePygame(gameName):
    pygame.init()

    global SCREEN_WIDTH, SCREEN_HEIGHT, FPS, SCREEN_BUFFER
    SCREEN_WIDTH, SCREEN_HEIGHT = 2500, 1200
    FPS = 60
    SCREEN_BUFFER = 500

    global pygameKeyValues, inputNames, isCurrentInputs
    pygameKeyValues = [pygame.K_w, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_e, pygame.K_r]
    inputNames = ("moveUp", "moveLeft", "moveDown", "moveRight", "equip1", "equip2", "equip3", "interact", "reload")
    isCurrentInputs = [False for i in range(len(pygameKeyValues))]

    global gameWindow, clock
    gameWindow = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(gameName)
    clock = pygame.time.Clock()

    global triggerWeapon
    triggerWeapon = False

    global font
    font = pygame.font.Font('freesansbold.ttf', 30)





""" INPUT HANDLING"""
def handleEvents(mousePos):
    for event in pygame.event.get():
        """ CLOSE BUTTON """
        if event.type == pygame.QUIT:
            pygame.quit()
            return False
        """ KEYBOARD INPUTS """
        if event.type == pygame.KEYDOWN:
            for i, keyName in enumerate(pygameKeyValues): #For all inputs
                if event.key == keyName:
                    isCurrentInputs[i] = True
        elif event.type == pygame.KEYUP:
            for i, keyName in enumerate(pygameKeyValues): #For all inputs
                if event.key == keyName:
                    isCurrentInputs[i] = False
        
        """ MOUSE INPUTS """
        setMousePos(mousePos, pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0] == True:
                global triggerWeapon
                triggerWeapon = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if pygame.mouse.get_pressed()[0] == False:
                triggerWeapon = False
    return True, mousePos

def isInput(name):
    return isCurrentInputs[inputNames.index(name)]

def getInputNames():
    return inputNames

def getInputStates():
    return isCurrentInputs

def weaponTriggered():
    return triggerWeapon

def getScreenHeight():
    return SCREEN_HEIGHT

def getFont():
    return font

def getGameWindow():
    return gameWindow

def getClock():
    return clock

def setMousePos(oldMousePos, newMousePos):
    for i in range(len(oldMousePos)):
        oldMousePos[i] = newMousePos[i]

def setWeaponTriggered(triggered):
    global triggerWeapon
    triggerWeapon = triggered


""" OTHER """

def drawGame(background, entities, hudElements):
    gameWindow.fill(pygame.Color('black'))
    for i in background:
        i.drawObject(gameWindow)
    for i in entities:
        i.drawEntity(gameWindow)
    for i in hudElements:
        i.drawElement(gameWindow)
    pygame.display.update()

def centerAround(entity, allObjects):
    shift = entity.getDifferenceVector([SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2])
    for gameObject in allObjects:
        gameObject.addPos(shift)

def getRandomLocation():
    return [random.randrange(-SCREEN_BUFFER, SCREEN_WIDTH + SCREEN_BUFFER)
            , random.randrange(-SCREEN_BUFFER, SCREEN_HEIGHT + SCREEN_BUFFER)]
