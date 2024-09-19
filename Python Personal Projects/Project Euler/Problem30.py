validNumbers = []

for i in range(2, 999999):
    numString = str(i)
    sumPowers = 0
    for j in numString:
        sumPowers += int(j) ** 5
    if i == sumPowers:
        validNumbers.append(i)

print(validNumbers)
print(sum(validNumbers))