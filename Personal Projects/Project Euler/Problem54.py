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

class hand:
    def __init__(self, priority, name, extra = ()):
        self._priority = priority
        self._name = name
        self._extra = extra

    def getPriority(self):
        return self._priority
    
    def getName(self):
        return self._name
    
    def getExtra(self):
        return self._extra


def getHighCard(cardValues):
    highestCardIndex = -1
    for i in cardValues:
        cardIndex = cardValueList.index(i)
        if cardIndex > highestCardIndex:
            highestCardIndex
    return cardValueList[highestCardIndex]

def getValue(handList):
    allSameSuit = True
    for card in handList:
        if card != handList[0][1]:
            allSameSuit = False
    
    cardValues = ""
    for card in handList:
        cardValues += card[0]

    repeatValueCount = [0 for i in range(0, 13)]
    for i in cardValues:
        cardIndex = cardValueList.index(i)
        repeatValueCount[cardIndex] += 1


    consecutiveValues = True
    for i in range(1, 5):
        leftCardIndex = cardValueList.index(cardValues[i - 1])
        rightCardIndex = cardValueList.index(cardValues[i])
        if cardValueList[leftCardIndex] != cardValueList[rightCardIndex - 1]:
            consecutiveValues = False
    
    #return (Priority, Name, highCard,)
    if allSameSuit and set(cardValues) == set('T', 'J', 'Q', 'K', 'A'):
        return hand(1, 'Royal Flush')
    if allSameSuit and consecutiveValues:
        return hand(2, 'Straight Flush', getHighCard(cardValues))
    if 4 in repeatValueCount:
        fourPosition = repeatValueCount.index(4)
        fourValue = cardValueList[fourPosition]
        onePosition = repeatValueCount.index(1)
        nextHighest = cardValueList[onePosition]
        return hand(3, 'Four', fourValue, nextHighest)
    if 3 in repeatValueCount and 2 in repeatValueCount:
        threePosition = repeatValueCount.index(3)
        threeValue = cardValueList[threePosition]
        pairPosition = repeatValueCount.index(2)
        pairValue = cardValueList[pairPosition]
        return hand(4, 'Full House', (threeValue, pairValue))
    if allSameSuit:
        return hand(5, 'Flush', cardValues)
    if consecutiveValues:
        return hand(6, 'Straight', getHighCard(cardValues))
    if 3 in repeatValueCount:
        threePosition = repeatValueCount.index(3)
        threeValue = cardValueList[threePosition]
        leftOverValues = cardValues
        leftOverValues.replace(threeValue, "")
        return hand(7, 'Three', (threeValue, leftOverValues))
    if repeatValueCount.count(2) == 2:
        pass
    if 2 in repeatValueCount:
        pass
    return (10, 'High Card', cardValues)
    
    

def getWinner(p1Hand, p2Hand):
    pass

p1Wins = 0

for hand in handsStore:
    p1Hand = hand[0]
    p2Hand = hand[1]
    if getWinner(p1Hand, p2Hand) == 1:
        p1Wins += 1
