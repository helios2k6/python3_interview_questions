def saveMemo(memo, denomination, amount, combos):
    if amount in memo:
        savedAmount = memo[amount]
        savedAmount[denomination] = combos
    else:
        memo[amount] = {denomination: combos}

def getMemo(memo, denomination, amount):
    if amount in memo:
        savedAmount = memo[amount]
        if denomination in savedAmount:
            return savedAmount[denomination]
    return None

def changeImpl(memo, denominations, index, amountToFill):
    if index == len(denominations):
        return 1

    denomination = denominations[index]
    savedMemoAmount = getMemo(memo, denomination, amountToFill)

    if savedMemoAmount:
        return savedMemoAmount

    maxCoinsWeCanUse = amountToFill // denomination
    numCombos = 0
    for i in range(0, maxCoinsWeCanUse + 1):
        remainingAmount = amountToFill - (i * denomination)
        numCombos += changeImpl(memo, denominations, index + 1, remainingAmount)

    saveMemo(memo, denomination, amountToFill, numCombos)
    return numCombos

def change(amountToFill):
    denoms = [25, 10, 5]
    memo = {}
    return changeImpl(memo, denoms, 0, amountToFill)

def testImpl(amount, expect):
    combos = change(amount)
    print(f"Change for {amount}. Expect: {expect}. Got: {combos}")

def test1():
    testImpl(5, 2)

def test2():
    testImpl(10, 4)

def test3():
    testImpl(25, 13)

def test4():
    testImpl(120, 382)

def test5():
    testImpl(2000, 1103021)

test1()
test2()
test3()
test4()
test5()