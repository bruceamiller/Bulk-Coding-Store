from Useful_Funcs import *

def getAll(font, screenSizeAdjustment, classInfoTriads):
    windows = []
    text = []

    """ DATE & TIME WINDOW"""
    windows.append(WindowElement([0.0, 0.0], [0.2, 0.22]))
    
    text.append(TextElement(font, getWeekday, [0.095, 0.035]))
    text.append(TextElement(font, getDate, [0.095, 0.09]))
    text.append(TextElement(font, getClockText, [0.095, 0.145], letterSpacing = 20 * screenSizeAdjustment))

    """ CLASS COUNTDOWN WINDOW"""
    windows.append(WindowElement([0.75, 0.0], [0.25, 0.725]))
    
    text.append(TextElement(font, getTimeTillClassesText, [0.875, 0.035], letterSpacing = 20 * screenSizeAdjustment, verticalSpacing = 40, inputForUpdateTextFunc = classInfoTriads))
 


    return windows, text