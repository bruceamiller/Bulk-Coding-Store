#Check for numbers a * b = c, if the digits of all of them could be picked only once from 1-9. Sum all values of c where this is possible.

import math

def getDivisors(number):
    divisors = [1, number]
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            if i in divisors or number // i in divisors:
                return sorted(divisors)
            elif i == number // i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(number // i)
    return sorted(divisors)

sum = 0
for i in range(2, 100000):
    panDigits = set()
    repeatingDigits = False
    for digit in str(i):
        if digit in panDigits:
            repeatingDigits = True
        else:
            panDigits.add(digit)
    if not repeatingDigits:
        divisors = getDivisors(i)
        for multipleSet in range(len(divisors) // 2):
            repeatingDigits = False
            divisorPanDigits = set()
            multiplesString = str(divisors[multipleSet]) + str(divisors[len(divisors) - 1 - multipleSet])
            if len(divisors) % 2 == 0:
                for digit in multiplesString:
                    if digit in panDigits or digit in divisorPanDigits:
                        repeatingDigits = True
                    else:
                        divisorPanDigits.add(digit)
            cumulativeDigits = set(panDigits | divisorPanDigits)
            if cumulativeDigits == {'1', '2', '3', '4', '5', '6', '7', '8', '9'} and not repeatingDigits:
                sum += i
                break

print(sum)