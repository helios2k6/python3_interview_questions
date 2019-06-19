import sys

class Transaction:
    def __init__(self, a: int, b: int, summand: int) -> None:
        self.a = a
        self.b = b
        self.summand = summand

def arrayManipulation(transactions: list) -> int:
    trackingMap = {}
    maxNumber = None
    for transaction in transactions:
        if transaction.a not in trackingMap:
            trackingMap[transaction.a] = 0
        if transaction.b + 1 not in trackingMap:
            trackingMap[transaction.b + 1] = 0
        # mark the tracking map
        trackingMap[transaction.a] += transaction.summand
        trackingMap[transaction.b + 1] -= transaction.summand

        # determine the max number
        if not maxNumber:
            maxNumber = transaction.b
        elif maxNumber < transaction.b:
            maxNumber = transaction.b

    largestSumInInterval = 0
    runningSum = 0
    for i in range(0, maxNumber + 1):
        runningSum += trackingMap[i] if i in trackingMap else 0
        if runningSum > largestSumInInterval:
            largestSumInInterval = runningSum

    return largestSumInInterval

def test0():
    print(arrayManipulation([
        Transaction(1, 2, 1),
        Transaction(2, 3, 1),
    ]))

test0()