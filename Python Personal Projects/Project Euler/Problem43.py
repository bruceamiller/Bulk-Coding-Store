def getPermutations(head, numberStr):
    permutations = []
    if len(numberStr) == 2:
        permutations.extend([numberStr, numberStr[::-1]])
    else:
        for i in numberStr:
            for lowerPermutation in getPermutations(i, numberStr.replace(i, '')):
                permutations.append(i + lowerPermutation)
    return permutations

def allDivisible(numberStr):
    for i in range(7):
        numberSection = numberStr[1+i:4+i]
        if int(numberSection) % divisors[i] != 0:
            return False
    return True

panDigits= '9876543210'
permutationsList = getPermutations('', panDigits)

divisors = [2, 3, 5, 7, 11, 13, 17]

sum = 0
for numberStr in permutationsList:
    if allDivisible(numberStr):
        sum += int(numberStr)

print(sum)