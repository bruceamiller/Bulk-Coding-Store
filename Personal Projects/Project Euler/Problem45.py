
ACCURACY = 10000000000000

triangleValues = [1]
tN = 1

pentagonalValues = [1]
pN = 1

hexagonalValues = [1]
hN = 1
hexagonalNumber = 0

while hexagonalNumber < ACCURACY:
    hN += 1
    hexagonalNumber = hN * (3 * hN - 1) // 2
    while triangleValues[len(triangleValues) - 1] < hexagonalNumber:
        tN += 1
        triangleNumber = tN * (tN + 1) // 2
        triangleValues.append(triangleNumber)
    while pentagonalValues[len(pentagonalValues) - 1] < hexagonalNumber:
        pN += 1
        pentagonalNumber = pN * (3 * pN - 1) // 2
        pentagonalValues.append(pentagonalNumber)
    
    if hexagonalNumber in triangleValues and hexagonalNumber in pentagonalValues:
        print(hexagonalNumber)
    
    
