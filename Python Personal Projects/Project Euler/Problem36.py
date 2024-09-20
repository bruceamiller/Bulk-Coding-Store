#Find the sum all of all numbers < 1 Million that are a palindrome in both decimal and binary 

def reverseString(string):
    reversedText = ""
    for digit in reversed(string):
        reversedText += digit
    return reversedText


def isPalindrome(string):
    halfPoint = len(string) // 2
    if len(string) % 2 == 0 and string[:halfPoint] == reverseString(string[halfPoint:]):
        return True
    elif string[:halfPoint] == reverseString(string[halfPoint + 1:]):
        return True
    return False

sum = 0
for i in range(1, 1000000):
    decimalStr = str(i)
    binaryStr = bin(i).replace("0b", "")
    if isPalindrome(decimalStr) and isPalindrome(binaryStr):
        sum += i

print(sum)
