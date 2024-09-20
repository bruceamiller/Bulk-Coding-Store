def sumDigits(num):
    numStr = str(num)
    sum = 0
    for i in numStr:
        sum += int(i)
    return sum

largestSum = 0
for i in range(1, 100):
    for j in range(1, 100):
        currentSum = sumDigits(i ** j)
        if currentSum > largestSum:
            largestSum = currentSum

print(largestSum)