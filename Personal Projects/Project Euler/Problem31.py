#How many possible ways can you combine the coin values to get the target value?

def countCoinPermutations(coinSum, coinValues, largestCoin):
    permutations = 0
    newCoinValues = list(coinValues)
    coinChanged = True
    while coinChanged == True: #Remove unusable coins, or coins higher than last-used coin to prevent repeats.
        coinChanged = False
        if coinSum + newCoinValues[0] > targetValue or newCoinValues[0] > largestCoin:
            newCoinValues.remove(newCoinValues[0])
            coinChanged = True
    for coin in newCoinValues:
        if targetValue - coinSum == coin: #If the leftover room matches the value of the coin, then that is a completed coinSet.
            permutations += 1
            if len(newCoinValues) > 1:
                permutations += countCoinPermutations(coinSum, newCoinValues[1:], coin)
            break
        else: #If there is still room for more coins after that coin, then try again.
            permutations += countCoinPermutations(coinSum + coin, newCoinValues, coin)
    return permutations

targetValue = 200
coinValues = [200, 100, 50, 20, 10, 5, 2, 1]

print(countCoinPermutations(0, coinValues, float('inf')))