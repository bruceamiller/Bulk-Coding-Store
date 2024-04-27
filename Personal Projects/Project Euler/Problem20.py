factorial = 1
for i in range(1, 100):
    factorial *= i

sum = 0
for i in str(factorial):
    sum += int(i)

print(sum)