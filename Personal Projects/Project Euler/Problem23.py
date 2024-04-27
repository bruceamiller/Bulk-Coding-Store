def sumProperDivisors(number):
    divisors = [1, number]
    sum = 0
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            if i in divisors or number // i in divisors:
                divisors.remove(number)
                for d in divisors:
                    sum += d
                return sum
            elif i == number // i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(number // i)
    divisors.remove(number)
    for d in divisors:
        sum += d
    return sum





abundantList = []
for i in range(1, 18124):
    if sumProperDivisors(i) > i:
        abundantList.append(i)
print(abundantList)

abundantNumbers = set()
for i in range(1, 18124):
    if sumProperDivisors(i) > i:
        abundantNumbers.add(i)


def numIfCannotSum(i):
    for x in abundantNumbers:
        if i - x in abundantNumbers:
            return 0
    return i

sum = 0
for i in range(1, 18123):
    sumAddVal = numIfCannotSum(i)
    print(sumAddVal)
    sum += sumAddVal

print(sum)
