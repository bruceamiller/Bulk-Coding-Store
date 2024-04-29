import math

def isPrime(number):
    highestFactor = 1
    for i in range(2, round(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

maxConsecutivePrimes = 0

for a in range(-1000, 1001):
    for b in range(-1000, 1000):
        n = 0
        quadraticProduct = n ** 2 + a * n + b
        while quadraticProduct >= 0 and isPrime(quadraticProduct):
            n += 1
            quadraticProduct = n ** 2 + a * n + b
        if n > maxConsecutivePrimes:
            maxConsecutivePrimes = n
            answer = a * b

print(answer)
