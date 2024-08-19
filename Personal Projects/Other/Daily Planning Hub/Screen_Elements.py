from Useful_Funcs import *

def getAll(font, screenSizeAdjustment):
    windows = []
    text = []

    windows.append(WindowElement([0.0, 0.0], [0.2, 0.22]))
    
    text.append(TextElement(font, getWeekday, [0.095, 0.035]))
    text.append(TextElement(font, getDate, [0.095, 0.09]))
    text.append(TextElement(font, getClockText, [0.095, 0.145], letterSpacing = 20 * screenSizeAdjustment))
    


    return windows, text