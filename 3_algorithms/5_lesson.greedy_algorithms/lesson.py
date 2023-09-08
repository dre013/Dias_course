denominations = [1, 2, 5, 10, 20, 50, 100]

def returnChange(change, denominations):
    toGiveBack = [0] * len(denominations)

    for pos, coin in enumerate(reversed(denominations)):
        while coin <= change:
            change = change - coin
            toGiveBack[pos] += 1
    return(toGiveBack)

print(returnChange(60, denominations))