#Sum all numbers that equal the sum of the factorial of each of their digits

sum = 0
for i in range(3, 100000):
    factorialSum = 0
    for j in str(i):
        factorial = 1
        for k in range(1, int(j) + 1):
            factorial *= k
        factorialSum += factorial
    if factorialSum == i:
        sum += i

print(sum)