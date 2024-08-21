import math
"""
def isPrime(number):
    try:
        for i in range(2, round(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
    except:
        pass
    return True

Too slow

def getPrimeDivisors(number):
    divisors = []
    if number == 1:
        return [1]
    if isPrime(number):
        return [number]    
    for i in range(2, number + 1):
        if number % i == 0 and i != number:
            divisors.append(i)
            divisors.extend(getPrimeDivisors(number // i))
            break
        elif number == i:
            return [number]
    return divisors


def greatestCommonDenominator(numA, numB):
    aDivisors = getPrimeDivisors(numA)
    bDivisors = getPrimeDivisors(numB)
    commonDenominator = 1
    hasCommon = True
    while hasCommon:
        hasCommon = False
        for d in aDivisors:
            if d in bDivisors:
                commonDenominator *= d
                aDivisors.remove(d)
                bDivisors.remove(d)
                hasCommon = True
                break
    return commonDenominator
"""

#def greatestCommonDenominator(numA, numB)

class fraction:
    def __init__(self, numerator, denominator):
        self._n = numerator
        self._d = denominator
        commonFactor = math.gcd(self._n, self._d)
        self._n = self._n // commonFactor
        self._d = self._d // commonFactor
    
    def __add__(self, obj2):
        newNumerator = self._n * obj2._d + obj2._n * self._d
        newDenominator = self._d * obj2._d
        return fraction(newNumerator, newDenominator)

    def inverted(self):
        return fraction(self._d, self._n)
    
    def __str__(self):
        return f"({self._n}/{self._d})"
    
    def getNumerator(self):
        return self._n

    def getDenominator(self):
        return self._d

moreDigitNumerators = 0

currentFraction = fraction(1, 1)
for i in range(1000):
    currentFraction = currentFraction + fraction(1, 1)
    currentFraction = currentFraction.inverted()
    currentFraction = currentFraction + fraction(1, 1)

    currentNumerator = currentFraction.getNumerator()
    currentDenominator = currentFraction.getDenominator()
    if len(str(currentNumerator)) > len(str(currentDenominator)):
        print(currentFraction)
        moreDigitNumerators += 1

print(moreDigitNumerators)
