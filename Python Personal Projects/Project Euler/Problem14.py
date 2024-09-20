#Collatz Problem, longest chain for number < 1 Million


longestChain = 1
longestChainNumber = 1
for i in range(1000000, 0, -1):
    currentChainNumber = i
    chainLength = 0
    while i != 1:
        if i % 2 == 0:
            i = i // 2
            chainLength += 1
        else:
            i = i * 3 + 1
            chainLength += 1
    if chainLength >= longestChain:
        longestChain = chainLength
        longestChainNumber = currentChainNumber

print(longestChainNumber)