def factorial(n):
    factor = 1
    for i in range(1, n + 1):
        factor *= i
    return factor

def selectRFromN(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

totalCombinations = 0

for n in range(1, 101):
    r = 1
    combinations = []
    while r <= n:
        r += 1
        combinations.append(selectRFromN(n, r))
    for i in combinations:
        if i > 1000000:
            totalCombinations += 1




print(totalCombinations)