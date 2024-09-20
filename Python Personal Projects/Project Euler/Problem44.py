

pentagonalValues = set()

n = 0
pentagonalNumber = 0
while pentagonalNumber < 10000000:
    n += 1
    pentagonalNumber = n * (3 * n - 1) // 2
    pentagonalValues.add(pentagonalNumber)

smallestDifference = float('inf')

for j in pentagonalValues:
    for k in pentagonalValues:
        if j + k in pentagonalValues and j - k in pentagonalValues:
            absoluteDifference = abs(k-j)
            if absoluteDifference < smallestDifference:
                smallestDifference = absoluteDifference

print(smallestDifference)