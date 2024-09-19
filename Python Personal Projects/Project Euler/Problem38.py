pandigitalNumbers = []

longestNumber = 0
lengthLongestNumber = 0

largestPandigital = 0

for rootNumber in range(2, 10000):
    pandigitalProduct = ""
    panDigits = set()

    nonRepeating = True

    for consecutiveInts in range(1, 10):
        productStr = str(rootNumber * consecutiveInts)
        for digit in productStr:
            if digit in panDigits:
                nonRepeating = False
            else:
                panDigits.add(digit)
                pandigitalProduct += digit
        if consecutiveInts > 1 and nonRepeating and panDigits == {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            if int(pandigitalProduct) > largestPandigital:
                largestPandigital = int(pandigitalProduct)
            break

print(largestPandigital)