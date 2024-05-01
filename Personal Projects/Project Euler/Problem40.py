#Concatenate all positive integers. What is the product of: the 1st, 10th, 100th..., 1000000th digit.

concatenatedLength = 0

currentNumber = 0

digits = []

for i in range(0, 7):
    NthDigit = 10 ** i
    while concatenatedLength < NthDigit:
        currentNumber += 1
        currentStr = str(currentNumber)
        concatenatedLength += len(currentStr)
    digits.append(int(currentStr[len(currentStr) - (concatenatedLength - NthDigit) - 1]))

print(digits)

product = 1
for i in digits:
    product *= i

print(product)