file = open("C:\\Users\\Bruce\\Documents\\GitHub\\Python-Coding\\Personal Projects\\Project Euler\\Problem13.txt")

numbers = []
for line in file.readlines():
    numbers.append(line.strip())
file.close


digitSums = []
for digit in range(0, 50):    
    currentDigitSum = 0
    for line in numbers:
        currentDigitSum += int(line[digit])
    digitSums.append(currentDigitSum)

print(digitSums)

#Get first ten digits~
digits = 0
leadingNum = digitSums[0]
for i in range(1, 12):
    leadingNum = leadingNum * 10 + digitSums[i]

print(leadingNum)