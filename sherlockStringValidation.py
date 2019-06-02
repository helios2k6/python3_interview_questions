def isValid(s):
    counts = {}
    for c in s:
        if c not in counts:
            counts[c] = 0
        counts[c] = counts[c] + 1

    uniqueCounts = {}
    for char, count in counts.items():
        if count not in uniqueCounts:
            uniqueCounts[count] = 0
        uniqueCounts[count] = uniqueCounts[count] + 1

    lengthOfUniqueCounts = len(uniqueCounts)
    if lengthOfUniqueCounts == 1:
        return "YES"
    if lengthOfUniqueCounts > 2:
        return "NO"

    firstNumber = None
    firstNumberCount = None
    secondNumber = None
    secondNumberCount = None
    for count, numberOfCount in uniqueCounts.items():
        if not firstNumber:
            firstNumber = count
            firstNumberCount = numberOfCount
        else:
            secondNumber = count
            secondNumberCount = numberOfCount

    biggerNumber = None
    biggerNumberCount = None
    smallerNumber = None
    smallerNumberCount = None

    if firstNumber > secondNumber:
        biggerNumber = firstNumber
        biggerNumberCount = firstNumberCount
        smallerNumber = secondNumber
        smallerNumberCount = secondNumberCount
    else:
        biggerNumber = secondNumber
        biggerNumberCount = secondNumberCount
        smallerNumber = firstNumber
        smallerNumberCount = firstNumberCount

    if biggerNumberCount > 1:
        if smallerNumber == 1 and smallerNumberCount == 1:
            return "YES"
        return "NO"

    if biggerNumber - 1 > smallerNumber:
        return "NO"

    return "YES"

def test0():
    print(isValid("aabbcd"))

def test1():
    print(isValid("aaaabbcc"))

def test2():
    print(isValid("aaaabbbcc"))

def test3():
    print(isValid("aaaabbbcccc"))

def test4():
    print(isValid("aacbb"))

test0()
test1()
test2()
test3()
test4()