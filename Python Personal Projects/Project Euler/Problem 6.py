squareOfSum = 0
for i in range(101):
    squareOfSum += i
squareOfSum = squareOfSum ** 2


sumOfSquares = 0
for i in range(101):
    sumOfSquares += i ** 2


difference = squareOfSum - sumOfSquares
print(f"{squareOfSum} - {sumOfSquares} = {difference}")