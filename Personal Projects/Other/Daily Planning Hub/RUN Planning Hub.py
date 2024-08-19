import time, pygame, os
from Useful_Funcs import *
import Screen_Elements

""" SYSTEM STARTUP """

pygame.init()

screen = pygame.display.set_mode((1200, 800), pygame.RESIZABLE)
screenMinWidth = 300
screenMinHeight = 300

pygame.display.set_caption('Daily Hub')


lastTimeText = getCurrentTime()
os.system('cls')

font = pygame.font.Font('freesansbold.ttf', 32)
currentFontSize = 32

""" LOAD INFO """

windows, text = Screen_Elements.getAll(font, 1)

""" MAIN LOOP """


mainLoopContinue = True
while mainLoopContinue:

    """ CONSOLE PRINT DATE. TIME. ETC. """
    if getCurrentTime() != lastTimeText:
        lastTimeText = getCurrentTime()
        os.system('cls')
        print(lastTimeText)

    """ UPDATE FONT SIZE & Spacing"""
    screenCurrentWidth, screenCurrentHeight = screen.get_size()
    standardFontSize = maxFontSizeFromWidth = maxFontSizeFromHeight = 32
    maxScreenSizeAdjustment = 1
    if screenCurrentWidth < 1278:
        maxFontSizeFromWidth = int(screenCurrentWidth / 1278 * 32)
        maxScreenSizeAdjustment = screenCurrentWidth / 1278
    elif screenCurrentHeight < 668:
        maxFontSizeFromHeight = int(screenCurrentHeight / 668 * 32)
        maxScreenSizeAdjustment = screenCurrentWidth / 668
    if  maxFontSizeFromWidth < maxFontSizeFromHeight:
        smallestFontSizeNeededForScreen = maxFontSizeFromWidth
    else:
        smallestFontSizeNeededForScreen = maxFontSizeFromHeight
    if smallestFontSizeNeededForScreen != currentFontSize:
        currentFontSize = smallestFontSizeNeededForScreen
        font = pygame.font.Font('freesansbold.ttf', currentFontSize)
        windows, text = Screen_Elements.getAll(font, maxScreenSizeAdjustment)


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