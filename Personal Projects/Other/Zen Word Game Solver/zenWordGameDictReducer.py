readFile = open("C:\\Users\\Bruce\\Documents\\GitHub\\Python-Coding\\Personal Projects\\Other\\Zen Word Game Solver\\words.txt")
writeFile = open("C:\\Users\\Bruce\\Documents\\GitHub\\Python-Coding\\Personal Projects\\Other\\Zen Word Game Solver\\validWords.txt", "w")

maxLength = 6

for wordLine in readFile.readlines():
    if len(wordLine) <= maxLength + 1 and wordLine.replace("\n", "").isalpha():
        writeFile.write(wordLine.lower())

print("Valid Words Finished.")