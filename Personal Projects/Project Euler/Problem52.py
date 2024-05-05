def countDigits(numberStr):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    numberCount = [0 for x in range(10)]
    for i in numberStr:
        numberCount[numbers.index(i)] += 1
    return numberCount

x = 0
allSame = False
while allSame == False:
    x += 1
    allSame = True
    for i in range(2, 7):
        if countDigits(str(x * i)) != countDigits(str(x)):
            allSame = False
            break

print(x)