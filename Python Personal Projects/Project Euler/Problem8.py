file = open("C:\\Users\\Bruce\\Documents\\GitHub\\Python-Coding\\Personal Projects\\Project Euler\\Problem8.txt")
numText = ""
for line in file.readlines():
    numText += line.strip()

greatestProduct = 1
for currentLeft in range(len(numText) - 13):
    newProduct = 1
    for currentPos in range(13):
        newProduct *= int(numText[currentLeft + currentPos])
    if newProduct >= greatestProduct:
        greatestProduct = newProduct

print(greatestProduct)
