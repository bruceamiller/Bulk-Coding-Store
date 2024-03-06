#
# Machine Problem 3
# CSCI 1300
# Bruce Miller
#
# Description:
# Get random equation: inputs, equation type
# Solve equation for answer
# Print answer and get input
# Check user input with computed answer and respond accordingly
# Print total right and wrong answers
# Ask user if continue problem
#

from random import randint, choice

print('MATH PRACTICE PROBLEMS')
print()
print('Add, Subtract, or Multiply the numbers together.')
print("I'll tell you if you are right or wrong.")
print()

newProblem = True
problemNum = 1
right = 0
wrong = 0

while newProblem:
    a = randint(0, 20)
    b = randint(0, 20)
    equation = choice(('+', '-', '*'))

    if equation == '+':
        answer = a + b
    elif equation == '-':
        answer = a - b
    elif equation == '*':
        answer = a * b

    equationStr = str(a) + ' ' + equation + ' ' + str(b) + ' = '
    inputString = 'Problem ' + str(problemNum) + ': ' + equationStr
    userAnswer = input(inputString)
    if userAnswer == str(answer):
        print("You are right!")
        right += 1
    else:
        print("Sorry, that is not correct. The correct answer is", str(answer) + '.')
        wrong += 1

    print()
    print("So far...", right, 'right', wrong, 'wrong.')
    print()
    newProblem = input("Do you want to  do another problem? ('Y' or 'N')").lower() in ('y', 'yes')
    problemNum += 1
