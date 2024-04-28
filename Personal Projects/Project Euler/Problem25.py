last = 1
current = 1
n = 2

while len(str(current)) != 1000:
    n += 1
    current, last = last + current, current

print(n)