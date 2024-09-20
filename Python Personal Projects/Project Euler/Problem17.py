singles = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def thousandsText(thousandsDigit):
    printText = ""
    if thousandsDigit > 0:
        printText += singles[thousandsDigit]
        printText += "thousand"
    return printText

def hundredsText(hundredsDigit):
    printText = ""
    if hundredsDigit > 0:
        printText += singles[hundredsValue]
        printText += "hundred"
    return printText

def tensText(tensValue = 0, singleValue = 0):
    printText = ""
    if tensValue == 1:
        printText += teens[singleValue]
    elif tensValue > 1:
        printText += tens[tensValue]
        if singleValue > 0:
            printText += singles[singleValue]
    elif singleValue > 0:
        printText += singles[singleValue]
    return printText

sumLetters = 0

for i in range(0, 1001):
    numText = str(i)

    singleValue = tensValue = hundredsValue = thousandValue = None
    if numText[-1:]:
        singleValue = int(numText[-1:])
    if numText[-2:-1]:
        tensValue = int(numText[-2:-1])
    if numText[-3:-2]:
        hundredsValue = int(numText[-3:-2])
    if numText[-4:-3]:
        thousandValue = int(numText[-4:-3])

    printText = ""
    if thousandValue:
        printText += thousandsText(thousandValue)
        if hundredsValue:
            printText += hundredsText(hundredsValue)
            if tensValue or singleValue:
                printText += "and"
                if tensValue and not singleValue:
                    printText += tensText(tensValue, 0)
                elif not tensValue and singleValue:
                    printText += tensText(0, singleValue)
                else:
                    printText += tensText(tensValue, singleValue)
    elif hundredsValue:
        printText += hundredsText(hundredsValue)
        if tensValue or singleValue:
            printText += "and"
            if tensValue and not singleValue:
                printText += tensText(tensValue, 0)
            elif not tensValue and singleValue:
                printText += tensText(0, singleValue)
            else:
                printText += tensText(tensValue, singleValue)
    elif tensValue or singleValue:
        if tensValue and not singleValue:
            printText += tensText(tensValue, 0)
        elif not tensValue and singleValue:
            printText += tensText(0, singleValue)
        else:
            printText += tensText(tensValue, singleValue)

    sumLetters += len(printText)
    print(printText, len(printText))

print(sumLetters)


