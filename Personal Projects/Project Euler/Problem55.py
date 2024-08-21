def reverseText(numberStr):
    newString = ""
    for i in reversed(numberStr):
        newString += i
    return newString

def isPalindrome(numberStr):
    if numberStr == reverseText(numberStr):
        return True
    return False

lychrelNums = 0

for i in range(1, 10000):
    if i == 349:
        pass
    palindrome = False
    newNumber = str(i)
    for j in range(50):
        reversedNum = reverseText(newNumber)
        newNumber = int(newNumber) + int(reversedNum)
        newNumber = str(newNumber)
        if isPalindrome(newNumber):
            palindrome = True
            break    
    if not palindrome:
        lychrelNums += 1


print(lychrelNums)