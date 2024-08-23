import pygame, random

""" CONCEPT: "Clicker" game where you buy keyboard keys to tap, instead of using the mouse."""

pygame.init()
defaultDisplaySize = (1200, 800)
screen = pygame.display.set_mode(defaultDisplaySize, pygame.RESIZABLE)
pygame.display.set_caption('Keyboard Collector')

FPS = 60
clock = pygame.time.Clock()

""" KEY SETUP"""

currentFontSize = 30
font = pygame.font.Font('testfont.ttf', currentFontSize)

keyNames = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
keyInputs = [pygame.K_q, pygame.K_w, pygame.K_e, pygame.K_r, pygame.K_t, pygame.K_y, pygame.K_u, pygame.K_i, pygame.K_o, pygame.K_p, pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_j, pygame.K_k, pygame.K_l, pygame.K_z, pygame.K_x, pygame.K_c, pygame.K_v, pygame.K_b, pygame.K_n, pygame.K_m]
keyObjects = []
letterStorage = [0 for i in range(len(keyNames))]
unlockedKeys = ['w']

clickUpgradeNames = [""]
cornerPopups = []

keyboardTopLeft = [0.05, 0.265]
keySize = [0.08, 0.08]
horizontalSpacing = 0.01
verticalSpacing = 0.05
rowLeftOffset = 0.03
rowLengths = [10, 9, 7]


class key():
    def __init__(self, centerPos, keyName):
        self._topLeft = centerPos
        self._keyName = keyName
        self._locked = True
        self._pressed = False
    
    def unlock(self):
        self._locked = False
    
    def setPressed(self, pressedState):
        self._pressed = pressedState
    
    def draw(self, display):
        screenDimensions = screen.get_size()
        squareScale = (screenDimensions[0] + screenDimensions[1]) / 2
        if self._pressed:
            keyColor = pygame.Color("grey9")
        else:
            keyColor = pygame.Color("grey5")
        pygame.draw.rect(display, keyColor, pygame.Rect(self._topLeft[0], self._topLeft[1], keySize[0] * screenDimensions[0], keySize[1] * screenDimensions[0]))
        if not self._locked:
            text = font.render(self._keyName, True, pygame.Color("white"))
            textRect = text.get_rect()
            textRect.center = (self._topLeft[0] + keySize[0] * screenDimensions[0] / 2, self._topLeft[1] + keySize[1] / 4 * screenDimensions[0])
            screen.blit(text, textRect)

class Popup():
    def __init__(self, name, text, life = 2 * FPS):
        self._name = name
        self._text = text
        self._life = life
    
    def isNamed(self, checkName):
        if self._name == checkName:
            return True
        else:
            return False
    
    def setText(self, newText):
        self._text = newText

    def reduceLife(self):
        self._life -= 1

    def getLife(self):
        return self._life

    def getText(self):
        return self._text

def drawText(display, text, location, color = "white"):
    text = font.render(text, True, pygame.Color(color))
    textRect = text.get_rect()
    textRect.topleft = location
    display.blit(text, textRect)


def setKeyPositions():
    currentKey = 0
    screenDimensions = screen.get_size()
    for rowNum in range(len(rowLengths)):
        for keyNum in range(rowLengths[rowNum]):
            currentKeyPos = ((keyboardTopLeft[0] + ((horizontalSpacing + keySize[0]) * keyNum) + rowLeftOffset * rowNum) * screenDimensions[0], (keyboardTopLeft[1] + (verticalSpacing + keySize[1]) * rowNum) * screenDimensions[0])
            keyObjects.append(key(currentKeyPos, keyNames[currentKey]))
            currentKey += 1
setKeyPositions()

for k in unlockedKeys:
    keyObjects[keyNames.index(k)].unlock()

""" MAIN LOOP """

mainLoopContinue = True
while mainLoopContinue:

    screen.fill(pygame.Color('black'))
    for i, k in enumerate(keyObjects):
        k.draw(screen)
    screenDimensions = screen.get_size()
    drawText(screen, f"Keys: {sum(letterStorage)}", (0.05 * screenDimensions[0], 0.05 * screenDimensions[1]))
    for currentPopup in cornerPopups:
        drawText(screen, currentPopup.getText(), (0.8 * screenDimensions[0], 0.8 * screenDimensions[1]))
    pygame.display.update()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            mainLoopContinue = False
        if event.type == pygame.KEYDOWN:
            for i, k in enumerate(keyInputs):
                if event.key == k:
                    keyObjects[i].setPressed(True)
                    if keyNames[i] in unlockedKeys:
                        letterStorage[i] += 1
                        existingPopup = False
                        for currentPopup in cornerPopups:
                            if currentPopup.isNamed(keyNames[i]):
                                existingPopup = True
                                currentPopup.setText(f"{keyNames[i].upper()} x({letterStorage[i]})")
                        if not existingPopup:
                            cornerPopups.append(Popup(keyNames[i], f"{keyNames[i].upper()} x({letterStorage[i]})"))

        if event.type == pygame.KEYUP:
            for i, k in enumerate(keyInputs):
                if event.key == k:
                    keyObjects[i].setPressed(False)
    
    for currentPopup in cornerPopups:
        currentPopup.reduceLife()
        if currentPopup.getLife() < 0:
            cornerPopups.remove(currentPopup)
    
    clock.tick(FPS)

