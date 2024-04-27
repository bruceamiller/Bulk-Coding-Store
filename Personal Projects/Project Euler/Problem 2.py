def getFibonacci():
    fibonacci = [1, 2]
    newTerm = fibonacci[len(fibonacci) - 1] + fibonacci[len(fibonacci) - 2]
    while newTerm <= 4000000:
        fibonacci.append(newTerm)
        newTerm = fibonacci[len(fibonacci) - 1] + fibonacci[len(fibonacci) - 2]
    return fibonacci


sum = 0
for i in getFibonacci():
    if i % 2 == 0:
        sum += i
print(sum)