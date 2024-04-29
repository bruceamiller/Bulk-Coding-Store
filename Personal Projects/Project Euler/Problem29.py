noRepeats = set()
for a in range(2, 101):
    for b in range(2, 101):
        noRepeats.add(a ** b)

print(len(noRepeats))