# 31 ** 2 is the largest possible number that could sum with others to 1000
def getAnswer():
    for c in range(1000):
        for b in range(c-1):
            for a in range(b-1):
                if a ** 2 + b ** 2 == c ** 2 and a + b + c == 1000:
                    return(a * b * c)
                

print(getAnswer())
