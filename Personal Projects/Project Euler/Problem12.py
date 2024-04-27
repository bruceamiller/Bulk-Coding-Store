import math

def listDivisors(number):
    divisors = [1, number]
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            if i in divisors or number // i in divisors:
                return divisors
            else:
                divisors.append(i)
                divisors.append(number // i)
    return divisors

naturalNumber = 1
triangleNumber = 1
numDivisors = 1
while numDivisors <= 500:
    naturalNumber += 1
    triangleNumber += naturalNumber
    numDivisors = len(listDivisors(triangleNumber))
print(triangleNumber)