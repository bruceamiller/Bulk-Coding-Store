import time, pygame, os
from Useful_Funcs import *
import Screen_Elements

""" SYSTEM STARTUP """

pygame.init()

baselineScreenSize = (1278, 668)

screen = pygame.display.set_mode(baselineScreenSize, pygame.RESIZABLE)
screenMinWidth = 300
screenMinHeight = 300

pygame.display.set_caption('Daily Hub')


lastTimeText = getCurrentTime()
os.system('cls')

BaselineClockFontSize = 32
currentClockFontSize = 32
Clockfont = pygame.font.Font('freesansbold.ttf', currentClockFontSize)


""" LOAD INFO """

classInfoTriads = getClassInfo()

windows, text = Screen_Elements.getAll(Clockfont, 1, classInfoTriads)


""" MAIN LOOP """


mainLoopContinue = True
while mainLoopContinue:

    """ CONSOLE PRINT DATE. TIME. ETC. """
    """
    if getCurrentTime() != lastTimeText:
        lastTimeText = getCurrentTime()
        os.system('cls')
        print(lastTimeText)
    """

    """ UPDATE FONT SIZE & Spacing"""
    screenCurrentWidth, screenCurrentHeight = screen.get_size()
    standardFontSize = maxFontSizeFromWidth = maxFontSizeFromHeight = BaselineClockFontSize
    maxScreenSizeAdjustment = 1
    if screenCurrentWidth < baselineScreenSize[0]:
        maxFontSizeFromWidth = int(screenCurrentWidth / baselineScreenSize[0] * BaselineClockFontSize)
        maxScreenSizeAdjustment = screenCurrentWidth / baselineScreenSize[0]
    elif screenCurrentHeight < baselineScreenSize[1]:
        maxFontSizeFromHeight = int(screenCurrentHeight / baselineScreenSize[1] * BaselineClockFontSize)
        maxScreenSizeAdjustment = screenCurrentWidth / baselineScreenSize[1]
    if  maxFontSizeFromWidth < maxFontSizeFromHeight:
        smallestFontSizeNeededForScreen = maxFontSizeFromWidth
    else:
        smallestFontSizeNeededForScreen = maxFontSizeFromHeight
    if smallestFontSizeNeededForScreen != currentClockFontSize:
        currentClockFontSize = smallestFontSizeNeededForScreen
        Clockfont = pygame.font.Font('freesansbold.ttf', currentClockFontSize)
        windows, text = Screen_Elements.getAll(Clockfont, maxScreenSizeAdjustment, classInfoTriads)


    """ DRAW SCREEN """
    currentScreenSize = list(screen.get_size())

    screen.fill(pygame.Color("black"))
    for w in windows:
        w.drawElement(screen)
    for t in text:
        t.drawElement(screen)
    pygame.display.update()


    """ QUIT APP CHECK """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            mainLoopContinue = False
        elif event.type == pygame.VIDEORESIZE:
            if currentScreenSize[0] < screenMinWidth or currentScreenSize[1] < screenMinHeight:
                if currentScreenSize[0] < screenMinWidth:
                    currentScreenSize[0] = screenMinWidth
                if currentScreenSize[1] < screenMinHeight:
                    currentScreenSize[1] = screenMinHeight
                pygame.display.quit()
                screen = pygame.display.set_mode(currentScreenSize, pygame.RESIZABLE)