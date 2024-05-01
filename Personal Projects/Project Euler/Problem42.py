file = open("C:\\Users\\Bruce\\Documents\\GitHub\\Python-Coding\\Personal Projects\\Project Euler\\words.txt")

def getValue(letter):
    return ord(letter) - 64


wordStore = file.readlines()[0]
wordStore = wordStore.replace('"', "").replace(",", " ")
wordStore = wordStore.split()


triangleValues = []


n = 0
triangleNumber = 0
while triangleNumber < 1000:
    n += 1
    triangleNumber = n * (n + 1) // 2
    triangleValues.append(triangleNumber)

triangleWordCount = 0

for word in wordStore:
    wordSum = 0
    for letter in word:
        wordSum += getValue(letter)
    if wordSum in triangleValues:
        triangleWordCount += 1



print(triangleWordCount)

