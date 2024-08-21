file = open("C:\\Users\\Bruce\\Documents\\GitHub\\Python-Coding\\Personal Projects\\Project Euler\\0054_poker.txt")

lines = file.readlines()
handsStore = []
for i in range(len(lines)):
    lines[i] = lines[i].strip()
    lines[i] = lines[i].split()
    handsStore.append((tuple(lines[i][:5]), tuple(lines[i][5:])))
file.close()

print(handsStore)

cardValueList = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'K', 'Q', 'A')

def getHighCard(handList):
    highestCardIndex = -1
    for i in handList:
        cardIndex = cardValueList.index(i[0])
        if cardIndex > highestCardIndex:
            highestCardIndex = cardIndex
    return cardValueList[highestCardIndex]

def allSameSuit(handList):
    allSameSuit = True
    for card in handList:
        if card != handList[0][1]:
            allSameSuit = False
    return allSameSuit

def getCardValues(handList):
    cardValues = ""
    for card in handList:
        cardValues += card[0]

def getRepeatValues(handList):
    repeatValueCount = [0 for i in range(0, 13)]
    for i in handList:
        cardIndex = cardValueList.index(i[0])
        repeatValueCount[cardIndex] += 1

def allConsecutive(handList):
    isConsecutive = True
    for i in range(1, 5):
        leftCardIndex = cardValueList.index(handList[i - 1][0])
        rightCardIndex = cardValueList.index(handList[i][0])
        if cardValueList[leftCardIndex] != cardValueList[rightCardIndex - 1]:
            isConsecutive = False
    return isConsecutive    


def getP1Wins(p1Hand, p2Hand):
    p1CardValues = getCardValues(p1Hand)
    p2CardValues = getCardValues(p2Hand)
    p1HighCard = getHighCard(p1CardValues)
    p2HighCard = getHighCard(p2CardValues)
    if allSameSuit(p1Hand) and p1HighCard == 'A' and not 2 in p1CardValues:
        return True
    if allSameSuit(p2Hand) and p2HighCard == 'A' and not 2 in p2CardValues:
        return False
    

p1Wins = 0

for hand in handsStore:
    p1Hand = hand[0]
    p2Hand = hand[1]
    if getP1Wins(p1Hand, p2Hand):
        p1Wins += 1
