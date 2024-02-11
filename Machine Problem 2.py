#
# Machine Problem 2
# CSCI 1300
# Bruce Miller
#
# Description:
# Set numbers from 1-20 on two axis.
# Add/multiply along those axis to create a grid.
# Print the numbers in right-aligned columns.
#

print()
print("ADDITION TABLE 1-20")
print()

x_list = list(range(1,21))
y_list = list(range(1,21))

for x in [0]+x_list:
    for y in [0]+y_list:
        if x != 0 or y != 0:
            output = x + y
        else:
            output = "x"
        print(f"{output:>4}", end="")
    print("")

print()
print("MULTIPLICATION TABLE 1-20")
print()

for x in [0]+x_list:
    for y in [0]+y_list:
        output = x + y
        if x != 0 and y != 0:
            output = x * y
        elif x == 0 and y == 0:
            output = "x"
        else:
            output = x + y
        print(f"{output:>4}", end="")
    print()
