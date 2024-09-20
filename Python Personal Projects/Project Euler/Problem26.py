from decimal import *


def findRecurringNumbers(decString, layerDeep = 0):
    if len(decString) == precision - layerDeep:
        for i in range(1, (precision - layerDeep) // 2):
            if i == 34:
                pass
            matches = True
            if decString[:i] != decString[i:2*i]:
                matches = False
            else:
                for j in range(2, (precision - layerDeep) // i): #Check if repeating for whole rest of string
                    if decString[:i] != decString[j*i-i:j*i]:
                        matches = False
            if matches:
                return decString[:i]
        if layerDeep < 998: #Fix error if too many recursions
            return findRecurringNumbers(decString[1:], layerDeep + 1)
        else:
            return "NotProcessed2"
    elif layerDeep == 0:
        return ""
    else:
        return "NotProcessed1"

precision = 3000
getcontext().prec=precision + 1

lenLongestRecurring = 1

print(len(findRecurringNumbers(str(Decimal(1)/Decimal(983))[2:precision+2])))


notEnoughPrecision = []
tooManyRecursions = []


for i in range(2, 1000):
    currentDec = str(Decimal(1)/Decimal(i))[2:precision+2]
    recurringNumbers = findRecurringNumbers(currentDec)
    if recurringNumbers == "NotProcessed1":
        notEnoughPrecision.append(i)
    elif recurringNumbers == "NotProcessed2":
        tooManyRecursions.append(i)
    else:
        recurringLength = len(findRecurringNumbers(currentDec))
    if recurringLength > lenLongestRecurring:
        lenLongestRecurring = recurringLength
        valueLongestRecurring = i

print(valueLongestRecurring)
print("Not enough precision:", notEnoughPrecision)
print("tooManyRecursions:", tooManyRecursions)
