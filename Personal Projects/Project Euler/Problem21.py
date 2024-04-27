import math

def sumProperDivisors(number):
    divisors = [1, number]
    sum = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            if i in divisors or number // i in divisors:
                divisors.remove(number)
                for d in divisors:
                    sum += d
                return sum
            elif i == number // i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(number // i)
    divisors.remove(number)
    for d in divisors:
        sum += d
    return sum

sum = 0
for i in range(1, 10000):
    currentSum = sumProperDivisors(i)
    reverseSum = sumProperDivisors(currentSum)
    if reverseSum < 10000 and i == reverseSum and i != currentSum:
        sum += currentSum

print(sum)