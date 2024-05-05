import math

primes = 500000
#primes = 

def isPrime(number):
    if number == 1:
        return False
    for i in range(2, round(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def getAnswer(consecutivePrimes):
    mostConsecutive = 0

    for depth in range(0, len(consecutivePrimes)):
        for sectionLength in range(mostConsecutive - 1, depth + 2):
            for sectionLeft in range(depth - sectionLength + 2):
                section = consecutivePrimes[sectionLeft:sectionLeft + sectionLength]
                sumSection = sum(section)
                if isPrime(sumSection) and len(section) > mostConsecutive:
                    if sumSection < 1000000:
                        mostConsecutive = len(section)
                        answer = sumSection
                    else:
                        return answer

consecutivePrimes = [2]
for i in range(primes):
    currentNumber = i * 2 + 1
    if isPrime(currentNumber):
        consecutivePrimes.append(currentNumber)

#print(consecutivePrimes)
print("...")

print(getAnswer(consecutivePrimes))
