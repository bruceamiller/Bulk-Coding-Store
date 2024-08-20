import time, os, pygame

""" TEXT CONVERSION """

months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
monthsShortened = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
daysTextShortened = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

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

def textAfterFirstColon(line):
    resultText = ""
    readText = False
    for i in line:
        if readText:
            resultText += i
        elif i == ":":
            readText = True
    return resultText.strip()

def getClassInfo():
    file = open("c:\\Users\\Bruce\\Desktop\\Github Personal Project Data\\Planning Hub Info\\Class Schedule.txt")

    classInfoTriads = []
    currentClass = []

    for line in file.readlines():
        currentLineData = textAfterFirstColon(line)
        if line:
            if "Class Name:" in line:
                if currentClass:
                    classInfoTriads.append(currentClass)
                currentClass = []
                currentClass.append(currentLineData)
            if "Weekdays:" in line:
                currentClassWeekdays = []
                for day in daysTextShortened:
                    if day in currentLineData:
                        currentClassWeekdays.append(day)
                currentClass.append(currentClassWeekdays)
            if "Time:" in line:
                currentClass.append(currentLineData.split(" - "))
    classInfoTriads.append(currentClass)
    
    return classInfoTriads

def getTimeTillClassesText(classInfoTriads):
    currentTimeInfo = time.localtime()
    currentTimeTimer = WeeklyTimer(currentTimeInfo[6] + 1, currentTimeInfo[3], currentTimeInfo[4] ,currentTimeInfo[5])

    stringsToPrint = []

    coupletsToSortClasses = []

    for classInfo in classInfoTriads:
        stringsToPrint.append(classInfo[0])

        
        classPeriodStartTime = classInfo[2][0]

        timersTillEachClassDay = []

        for day in classInfo[1]:
            currentDayTimer = WeeklyTimer()
            classHour, classMinute = [int(i) for i in classPeriodStartTime.split(":")]
            
            currentDayTimer.addDays(daysTextShortened.index(day))

            currentDayTimer.addHours(classHour)
            currentDayTimer.addMinutes(classMinute)
            
            timerTillCurrentDay = currentDayTimer - currentTimeTimer
            timersTillEachClassDay.append(timerTillCurrentDay)

            #Make a timer for every class of the week. Subtract the current time timer from each of those timers. Whichever timer is the shortest for that class, is the shortest time till the next class period for that class.
            #THEN sort all classes by which is the closest to now, and display in order.
        
        shortestTimer = WeeklyTimer(6, 23, 59, 59)
        for timer in timersTillEachClassDay:
            if timer < shortestTimer:
                shortestTimer = timer
        stringsToPrint.append(str(shortestTimer))

    #After-the-fact hack to sort classes by shortest time till class.
    for i in range(len(stringsToPrint) // 2 - 1):
        for j in range(len(stringsToPrint) // 2 - 1):
            currentTimeLeft = [int(i) for i in stringsToPrint[j * 2 + 1].split(":")]
            currentTimeRight = [int(i) for i in stringsToPrint[(j+ 1) * 2 + 1].split(":")]
            if currentTimeLeft[0] > currentTimeRight[0] or (currentTimeLeft[0] == currentTimeRight[0] and currentTimeLeft[1] > currentTimeRight[1]):
                temp = stringsToPrint[j * 2], stringsToPrint[j * 2 + 1]
                stringsToPrint[j * 2], stringsToPrint[j * 2 + 1] = stringsToPrint[(j+ 1) * 2], stringsToPrint[(j+ 1) * 2 + 1]
                stringsToPrint[(j+ 1) * 2], stringsToPrint[(j+ 1) * 2 + 1] = temp

    return stringsToPrint



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
    def __init__(self, font, updateTextFunc = getTestText, relativePos = [0.0, 0.0], color = "white", letterSpacing = None, verticalSpacing = None, inputForUpdateTextFunc = None):

        self._font = font

        self._color = color
        
        self._updateTextFunc = updateTextFunc

        self._text = None
        self._rect = None
        
        self._relativePos = relativePos

        self._letterSpacing = letterSpacing

        self._verticalSpacing = verticalSpacing

        self._inputForUpdateTextFunc = inputForUpdateTextFunc
        
    def updateText(self):
        self._text = self._font.render(self._updateTextFunc(), True, pygame.Color(self._color))
    
    def drawElement(self, screen):
        screenSize = pygame.display.get_window_size()

        if self._verticalSpacing and self._letterSpacing:
            classesTextLines = self._updateTextFunc(self._inputForUpdateTextFunc)
            # If the line is a clock then the individual characters are spaced evenly to ignore number character width
            for lineNum, currentClassText in (enumerate(classesTextLines)):
                if currentClassText.replace(":", "").isnumeric():
                    centerWordPos = (self._relativePos[0] * screenSize[0], self._relativePos[1] * screenSize[1] + self._verticalSpacing * lineNum)
                    letterNum = len(currentClassText)
                    if letterNum % 2 == 0:
                        leftMost = centerWordPos[0] - (letterNum / 2 - 0.5) * self._letterSpacing
                    else:
                        leftMost = centerWordPos[0] - (letterNum - 1) / 2 * self._letterSpacing
                    for pos, letter in enumerate(currentClassText):
                        newLetterText = self._font.render(letter, True, pygame.Color(self._color))
                        newLetterRect = newLetterText.get_rect()
                        newLetterRect.center = (leftMost + pos * self._letterSpacing, centerWordPos[1])
                        screen.blit(newLetterText, newLetterRect)
                else:
                    newLineText = self._font.render(currentClassText, True, pygame.Color(self._color))
                    newLineRect = newLineText.get_rect()
                    newLineRect.center = (self._relativePos[0] * screenSize[0], self._relativePos[1] * screenSize[1] + self._verticalSpacing * lineNum)
                    screen.blit(newLineText, newLineRect)

        elif self._letterSpacing:
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

        elif self._verticalSpacing:
            classesTextLines = self._updateTextFunc(self._inputForUpdateTextFunc)
            for lineNum, currentClassText in enumerate(classesTextLines):
                newLineText = self._font.render(currentClassText, True, pygame.Color(self._color))
                newLineRect = newLineText.get_rect()
                newLineRect.center = (self._relativePos[0] * screenSize[0], self._relativePos[1] * screenSize[1] + self._verticalSpacing * lineNum)
                screen.blit(newLineText, newLineRect)

        else:
            self.updateText()
            self._rect = self._text.get_rect()
            self._rect.center = (screenSize[0] * self._relativePos[0], screenSize[1] * self._relativePos[1])
            screen.blit(self._text, self._rect)

"""
def courseInfo():
    def __init__(self, courseName, weekdays = [], time = "00:00 - 00:00"):
        self._courseName = courseName
        self._weekdays = weekdays
        self._time = time

    def getCourseName(self):
        return self._courseName

    def addWeekdays(self, weekdayStr):
        for day in daysTextShortened:
            if day in weekdayStr and not day in self._weekdays:
                self._weekdays.append(day)
    
    def getWeekdays(self):
        weekdayStr = ""
        for day in self._weekdays:
            weekdayStr += day + " "
        return weekdayStr
"""

class WeeklyTimer():
    
    def __init__(self, days = 0, hours = 0, minutes = 0, seconds = 0):
        self._days = days
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
    
    def addDays(self, daysToAdd):
        self._days += daysToAdd
        while self._days < 0:
            self._days += 7
        while self._days >= 7:
            self._days -= 7
    
    def addHours(self, hoursToAdd):
        self._hours += hoursToAdd % 24
        while self._hours < 0:
            self.addDays(-1)
            self._hours += 24
        while self._hours >= 24:
            self.addDays(1)
            self._hours -= 24
    
    def addMinutes(self, minutesToAdd):
        self._minutes += minutesToAdd % 60
        while self._minutes < 0:
            self.addHours(-1)
            self._minutes += 60
        while self._minutes >= 60:
            self.addHours(1)
            self._minutes -= 60
    
    def addSeconds(self, secondsToAdd):
        self._seconds += secondsToAdd % 60
        while self._seconds < 0:
            self.addMinutes(-1)
            self._seconds += 60
        while self._seconds >= 60:
            self.addMinutes(1)
            self._seconds -= 60
    
    def isNegativeTimer(self):
        if self._hours < 0:
            return True
        return False

    def __add__(self, other):
        newTimer = WeeklyTimer()
        newTimer.addDays(self._days + other._days)
        newTimer.addHours(self._hours + other._hours)
        newTimer.addMinutes(self._minutes + other._minutes)
        newTimer.addSeconds(self._seconds + other._seconds)

        return newTimer
    
    def __sub__(self, other):
        newTimer = WeeklyTimer()
        newTimer.addDays(self._days - other._days)
        newTimer.addHours(self._hours - other._hours)
        newTimer.addMinutes(self._minutes - other._minutes)
        newTimer.addSeconds(self._seconds - other._seconds)

        return newTimer
    
    def __gt__(self, other):
        #The same class on different days had to be hours apart, which is all I'm checking so I'm not going to program to check down to the seconds.
        if self._days > other._days:
            return True
        return False

    def __lt__(self, other):
        #The same class on different days had to be hours apart, which is all I'm checking so I'm not going to program to check down to the seconds.
        if self._days < other._days:
            return True
        return False
    
    def __str__(self):
        timeString = ""
        for timeSegment in (self._days, self._hours, self._minutes, self._seconds):
            if timeSegment < 10:
                timeString += "0" + str(timeSegment) + ":"
            else:
                timeString += str(timeSegment) + ":"
        return timeString[:len(timeString)-1]
        return f"{self._days}:{self._hours}:{self._minutes}:{self._seconds}"

        