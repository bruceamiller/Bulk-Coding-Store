file = open("C:\\Users\\Bruce\\Desktop\\Python Coding\\Personal Projects\\Project Euler\\0059_cipher.txt")
asciiCipher = file.read()
asciiCipher = asciiCipher.replace(',', ' ')
asciiCipher = asciiCipher.split()
for i in range(len(asciiCipher)):
    asciiCipher[i] = int(asciiCipher[i])
print(asciiCipher)
file.close()

def strFromCipher(list):
    cipherStr = ""
    for value in list:
        cipherStr += chr(value)
    return cipherStr

def XOR(valueA, valueB):
    valueA = bin(valueA)[2:]
    valueB = bin(valueB)[2:]
    valueC = ""
    if len(valueA) > len(valueB):
        valueB = "0" * (len(valueA) - len(valueB)) + valueB
    else:
        valueA = "0" * (len(valueB) - len(valueA)) + valueA
    for i in range(len(valueA)):
        if valueA[i] != valueB[i]:
            valueC += "1"
        else:
            valueC += "0"
    valueC = int(valueC, 2)
    return valueC

print(XOR(65, 42))


commonWords = ['a', 'the', ' ', 'then', 'and']

keyLetterMin = ord('a')
keyLetterMax = ord('z')

for x in range(keyLetterMin, keyLetterMax + 1):
    for y in range(keyLetterMin, keyLetterMax + 1):
        for z in range(keyLetterMin, keyLetterMax + 1):
            sumAscii = 0
            currentDeciphered = []
            password = [x, y, z]
            validPasswordOutput = True
            passwordPos = len(password) - 1
            for characterVal in asciiCipher:
                if passwordPos == len(password) - 1:
                    passwordPos = 0
                else:
                    passwordPos += 1
                decodedCharacterVal = XOR(characterVal, password[passwordPos])
                currentDeciphered.append(decodedCharacterVal)
                sumAscii += decodedCharacterVal
            cipherStr = strFromCipher(currentDeciphered)
            allWordsInSolution = True
            for word in commonWords:
                if not word in cipherStr:
                    allWordsInSolution = False
            if allWordsInSolution:
                print(password, sumAscii, "-", cipherStr)