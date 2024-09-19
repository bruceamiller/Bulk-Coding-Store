#Recursive, let's go!
def getPermutations(head, numberStr):
    permutations = []
    if len(numberStr) == 2:
        permutations.extend([numberStr, numberStr[::-1]])
    else:
        for i in numberStr:
            for lowerPermutation in getPermutations(i, numberStr.replace(i, '')):
                permutations.append(i + lowerPermutation)
    return permutations


print(getPermutations("", "0123456789")[999999])