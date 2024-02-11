#
# Machine Problem 1
# CSCI 1300
# Bruce Miller
#
# Description: This script prompts the user for their name, the year they were
# born, and the balance in their savings account. A greeting is output
# along with the projected year of retirement, and an estimate
# of what their savings account will be worth at that time. Three
# assumptions are made. (1) the current year is 2023, (2) retirement
# age is 65, and (3) the annual rate of growth for the savings
# account will be 7%.
#

currentYear = 2023
retirementAge = 65
annualGrowthRate = 1.07

print("\nLet's see how much money you will have when you retire.\n")

name = input("What is your name? ")
birthYear = int(input("What year were you born? "))
savingsBal = float(input("What is the balance of your savings account? "))

retirementDistance = ((birthYear + retirementAge) - currentYear) # years till retirement

print("\nHello,", name + "!")
print("You turn", (currentYear-birthYear), "this year.") # currentAge = currentYear - birthYear
print("You will retire in", str(birthYear + retirementAge) + ".") # retirementAge = birthYear + retirementAge
print("That will be", retirementDistance, "years from now.")
print("Congratulations! You will have", (savingsBal * annualGrowthRate ** retirementDistance), "by that time.\n")
