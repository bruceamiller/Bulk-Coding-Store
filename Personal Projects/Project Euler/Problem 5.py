def evenDivide(number):
    divisors = [11, 13, 14, 16, 17, 18, 19, 20] #Removed factors 1-20, whose factors were included in larger numbers.
    for i in divisors:
        if number % i != 0:
            return False
    return True

currentNumber = 1
outputFound = False
while not outputFound:
    if evenDivide(currentNumber):
        outputFound = True
        print(currentNumber)
    else:
        currentNumber += 1

#It takes about a minute to calculate. Is there a faster way?