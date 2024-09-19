file = open("C:\\Users\\Bruce\\Documents\\GitHub\\Python-Coding\\Personal Projects\\Other\\Zen Word Game Solver\\validWords.txt")

possibleInputLetters = input("Enter all letters on screen, including repeats: ")

wordLengths = []
for number in input("Enter possible word lengths: ").replace(" ", "").replace(",", ""):
    wordLengths.append(int(number))



for wordLine in file.readlines():
    currentLetterCache = possibleInputLetters
    currentWordLetterList = list(wordLine.replace("\n", ""))

    if len(currentWordLetterList) in wordLengths:
        for letter in currentLetterCache:
            if letter in currentWordLetterList:
                currentWordLetterList.remove(letter)
    
    if not currentWordLetterList:
        print(wordLine)