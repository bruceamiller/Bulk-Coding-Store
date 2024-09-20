def isPalindrome(number):
    numberString = str(number)
    reversedString = ""
    for i in range(1, len(numberString) + 1):
        reversedString += numberString[-i]
    if reversedString == numberString:
        return True
    else:
        return False




for x in range(100, 1000):
    for y in range(100, 1000):
        product = x * y
        try:
            if isPalindrome(product) and product > largestPalindrome:
                largestPalindrome = product
        except NameError:
            largestPalindrome = product


print(largestPalindrome)
