from database_classes import *
import os, random


""" USEFUL INFO

possibleStatuses = ["Unknown", "Incomplete", "Hiatus", "Complete"]
readInfo = ["Name", "Current Ch", "Comment", "Last Read", "Status"]

"""

""" EXPORT AND IMPORT FUNCTIONS """

def textAfterColon(line):
    returnText = ""
    readText = False
    for i in line:
        if readText:
            returnText += i
        elif i == ":":
            readText = True
    return returnText.strip().replace("\"", "")

def getAllManwha():
    manwhaReadStore = open("c:\\Users\\Bruce\\Desktop\\Current Watching Data\\Manwha Info.txt", 'r')
    allManwha = []

    currentManwha = None


    for line in manwhaReadStore.readlines():
        currentLineText = textAfterColon(line)
        if currentLineText:
            if "Name:" in line:
                if currentManwha:
                    allManwha.append(currentManwha)
                currentManwha = Manwha()
                currentManwha.setName(currentLineText)
            elif "Current Ch:" in line:
                currentManwha.setCurrentCh(currentLineText)
            elif "Comment:" in line:
                currentManwha.setComment(currentLineText)
            elif "Last Read:" in line:
                currentManwha.setLastRead(currentLineText)
            elif "Status:" in line:
                currentManwha.setStatus(currentLineText)
    allManwha.append(currentManwha)
    manwhaReadStore.close()
    return allManwha

def rewriteAll(allManwha):
    manwhaWriteStore = open("c:\\Users\\Bruce\\Desktop\\Current Watching Data\\Manwha Info.txt", 'w')
    for m in allManwha:
        manwhaWriteStore.write(str(m)+"\n\n")

""" MAIN LOOP FUNCTIONS """

def searchedList(searchTerm, allManwhaList):
    searchTerm = searchTerm.lower()
    searchedList = []
    for m in allManwhaList:
        manwhaName = m.getName().lower()
        if searchTerm in manwhaName:
            searchedList.append(m)
    return searchedList

""" TEXT FUNCTIONALITY """
def printAll(allManwha):
    for m in allManwha:
        print(m)
        print()

def printAllReversed(allManwha):
    for m in range(len(allManwha) - 1, -1, -1):
        print(allManwha[m])
        print()

def printAllNumbered(allManwha):
    print()
    currentNumber = 0
    for m in allManwha:
        currentNumber += 1
        print(str(currentNumber) + ".")
        print(m)
        print()

def searchAndPickOption(manwhaList):
    os.system('cls')
    print(""" --- SEARCH --- """)
    searchTerm = input("\nEnter search Term > ")
    searchOptions = searchedList(searchTerm, manwhaList)
    if searchTerm == "":
        return None
    elif len(searchOptions) == 1:
        return searchOptions[0]
    elif searchOptions:
        optionInput = 1
        while optionInput:
            os.system('cls')
            print(""" --- SEARCH --- """)
            print("\nEnter search Term >", searchTerm)
            printAllNumbered(searchOptions)
            optionInput = input("> ")
            if optionInput.isnumeric() and 0 < int(optionInput) <= len(searchOptions):
                optionSelectNum = int(optionInput)
                return searchOptions[optionSelectNum - 1]
            elif optionInput == "":
                return searchAndPickOption(manwhaList)
    else:
        print("No options found.")

def defaultIfEmptyInput(promptText, originalText): #Defaults to original text, if receives empty imput
    userText = input(promptText)
    if userText:
        return userText
    else:
        return originalText

def editManwha(manwha):
    remove = False
    editing = True
    while editing:
        os.system('cls')
        print(""" --- EDITING --- \n""")
        print(manwha)
        selectedEdit = input("""\n1. Name
2. Current Ch
3. Comment
4. Last Read
5. Status
6. Remove
7. EXIT
                               
> """)
        if selectedEdit == "1":
            manwha.setName(defaultIfEmptyInput("\nEnter name of manwha > ", manwha.getName()))
        elif selectedEdit == "2":
            manwha.setCurrentCh(defaultIfEmptyInput("\nEnter chapter currently on > ", manwha.getCurrentCh()))
        elif selectedEdit == "3":
            manwha.setComment(defaultIfEmptyInput("\nEnter Comment > ", manwha.getComment()))
        elif selectedEdit == "4":
            manwha.setLastRead(defaultIfEmptyInput("\nEnter last date read > ", manwha.getLastRead()))
        elif selectedEdit == "5":
            manwha.setStatus(defaultIfEmptyInput("\nEnter manwha completion status > ", manwha.getStatus()))
        elif selectedEdit == "6":
            remove = input(f"\nAre you sure you would like to remove {manwha.getName()} > ").lower() in ("y", "yes")
            if remove == True:
                editing = False
        elif selectedEdit == "7":
            editing = False
    return remove

allManwhaList = getAllManwha()


continueSearch = True
while continueSearch:
    os.system('cls')
    print(""" --- MAIN MENU --- """)
    homeMenuNav = input("""\n1. Browse Recent
2. Search Manga
3. Add Manga
4. Random Manga
5. Exit & Save
                        
> """)
    
    if homeMenuNav == "1": # BROWSE #
        os.system('cls')
        printAllReversed(allManwhaList)
        input("Enter to exit > ")
    
    elif homeMenuNav == "2": # SEARCH #
        manwha = searchAndPickOption(allManwhaList)
        if manwha:
            os.system('cls')
            print("Picked Manwha:\n")
            print(manwha)
            if input("\nWould you like to EDIT? > ").lower() in ("y", "yes"):
                cancel = editManwha(manwha)
                allManwhaList.remove(manwha)
                allManwhaList.insert(0, manwha)
                if cancel:
                    allManwhaList.remove(manwha)
                rewriteAll(allManwhaList)
    
    elif homeMenuNav == "3": # ADD NEW #
        newManwha = Manwha()
        os.system('cls')
        newManwha.setName(input("Name: "))
        newManwha.setCurrentCh(input("Current Ch: "))
        newManwha.setComment(input("Comment: "))
        newManwha.setLastRead(input("Last Read: "))
        newManwha.setStatus(input("Status: "))
        cancel = False
        if input("\nWould you like to EDIT? > ").lower() in ("y", "yes"):
            cancel = editManwha(newManwha)
        allManwhaList.insert(0, newManwha)
        if cancel:
            allManwhaList.remove(newManwha)
        rewriteAll(allManwhaList)

    elif homeMenuNav == "4": # RANDOM #
        newRandom = True
        while newRandom:
            os.system('cls')
            print(""" --- RANDOM PICK --- """)
            print(random.choice(allManwhaList))
            if input("\nPress only ENTER to reroll > "):
                newRandom = False


    elif homeMenuNav == "5": # EXIT #
        rewriteAll(allManwhaList)
        print("\nDatabase Saved!")
        continueSearch = False