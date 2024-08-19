import time, os, pygame

""" TEXT CONVERSION """

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
monthsShortened = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

""" STRING GET FUNCTIONS """

def getCurrentTime():
    currentTimeInfo = time.localtime()

    weekdayText = days[currentTimeInfo[6]]
    dateText = monthsShortened[currentTimeInfo[1] - 1] + ", " + str(currentTimeInfo[2]) + ", " + str(currentTimeInfo[0])

    currentTimeInfo = time.localtime()

    if currentTimeInfo[3] == 0:
        standardHourConvert = 12
    elif currentTimeInfo[3] > 12:
        standardHourConvert = currentTimeInfo[3] - 12
    else:
        standardHourConvert = currentTimeInfo[3]

    if len(str(standardHourConvert)) == 1:
        standardHourConvert = "0" + str(standardHourConvert)
    else:
        standardHourConvert = str(standardHourConvert)

    if len(str(currentTimeInfo[4])) == 1:
        minutesText = "0" + str(currentTimeInfo[4])
    else:
        minutesText = str(currentTimeInfo[4])


    if len(str(currentTimeInfo[5])) == 1:
        secondsText = "0" + str(currentTimeInfo[5])
    else:
        secondsText = str(currentTimeInfo[5])


    middayReference = "AM"
    if currentTimeInfo[3] >= 12:
        middayReference = "PM"

    clockText = str(standardHourConvert) + ":" + str(minutesText) + ":" + secondsText + " " + middayReference

    return weekdayText + "\n" + dateText + "\n" + clockText + "\n"

def getClockText():
    currentTimeInfo = time.localtime()

    if currentTimeInfo[3] == 0:
        standardHourConvert = 12
    elif currentTimeInfo[3] > 12:
        standardHourConvert = currentTimeInfo[3] - 12
    else:
        standardHourConvert = currentTimeInfo[3]

    if len(str(standardHourConvert)) == 1:
        standardHourConvert = "0" + str(standardHourConvert)
    else:
        standardHourConvert = str(standardHourConvert)

    if len(str(currentTimeInfo[4])) == 1:
        minutesText = "0" + str(currentTimeInfo[4])
    else:
        minutesText = str(currentTimeInfo[4])


    if len(str(currentTimeInfo[5])) == 1:
        secondsText = "0" + str(currentTimeInfo[5])
    else:
        secondsText = str(currentTimeInfo[5])


    middayReference = "AM"
    if currentTimeInfo[3] >= 12:
        middayReference = "PM"

    clockText = str(standardHourConvert) + ":" + str(minutesText) + ":" + secondsText + " " + middayReference


    return clockText

def getWeekday():
    currentTimeInfo = time.localtime()
    weekdayText = days[currentTimeInfo[6]]
    return weekdayText

def getDate():
    currentTimeInfo = time.localtime()
    dateText = monthsShortened[currentTimeInfo[1] - 1] + ", " + str(currentTimeInfo[2]) + ", " + str(currentTimeInfo[0])
    return dateText

def getTestText():
    return "test"

""" SCREEN DRAWING CLASSES """

class WindowElement():
    def __init__(self, relativePos = [0.0, 0.0], relativeSize = [0.1, 0.1], backColor = "grey5"):
        self._relativePos = relativePos
        self._relativeSize = relativeSize
        self._backColor = backColor

    def drawElement(self, screen):
        screenSize = pygame.display.get_window_size()
        pygame.draw.rect(screen, self._backColor, pygame.Rect(screenSize[0] * self._relativePos[0], screenSize[1] * self._relativePos[1], screenSize[0] * self._relativeSize[0], screenSize[1] * self._relativeSize[1]))

class TextElement():
    def __init__(self, font, updateTextFunc = getTestText, relativePos = [0.0, 0.0], color = "white", letterSpacing = None):

        self._font = font

        self._color = color
        
        self._updateTextFunc = updateTextFunc

        self._text = font.render(self._updateTextFunc(), True, pygame.Color(self._color))
        self._rect = self._text.get_rect()
        
        self._relativePos = relativePos

        self._letterSpacing = letterSpacing
        
    def updateText(self):
        self._text = self._font.render(self._updateTextFunc(), True, pygame.Color(self._color))
    
    def drawElement(self, screen):
        if self._letterSpacing:
            screenSize = pygame.display.get_window_size()
            letterStr = self._updateTextFunc()
            letterNum = len(letterStr)
            centerWordPos = (screenSize[0] * self._relativePos[0], screenSize[1] * self._relativePos[1])
            if letterNum % 2 == 0:
                leftMost = centerWordPos[0] - (letterNum / 2 - 0.5) * self._letterSpacing
            else:
                leftMost = centerWordPos[0] - (letterNum - 1) / 2 * self._letterSpacing
            for pos, letter in enumerate(letterStr):
                newLetterText = self._font.render(letter, True, pygame.Color(self._color))
                newLetterRect = newLetterText.get_rect()
                newLetterRect.center = (leftMost + pos * self._letterSpacing, centerWordPos[1])
                screen.blit(newLetterText, newLetterRect)
        else:
            screenSize = pygame.display.get_window_size()
            self._rect.center = (screenSize[0] * self._relativePos[0], screenSize[1] * self._relativePos[1])
            self.updateText()
            screen.blit(self._text, self._rect)