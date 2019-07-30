def compare(a: str, b: str, aIndex: int, bIndex: int):
    if a[aIndex] == b[bIndex]:
        return "C"
    elif str.upper(a[aIndex]) == b[bIndex]:
        return "L"
    elif str.islower(a[aIndex]):
        return "l"
    return False

def isAbbreviation(a: str, b: str) -> bool:
    if not a and not b:
        return True

    if not a or not b or len(a) < len(b):
        return False

    cache = [[None for _ in range(0, len(a))] for _ in range(0, len(b))]
    for bIndex in range(0, len(b)):
        for aIndex in range(bIndex, len(a)):
            if not cache[bIndex][aIndex]:
                cache[bIndex][aIndex] = compare(a, b, aIndex, bIndex)

    # Check cache
    for i in range(0, len(b)):
        isBConsumed = False
        for j in range(0, len(a)):
            if cache[i][j] == "C" or cache[i][j] == "L":
                isBConsumed = True
                break
        if not isBConsumed:
            return False

    for i in range(0, len(a)):
        isAConsumed = False
        for j in range(0, len(b)):
            if cache[j][i] == "C" or cache[j][i] == "L" or cache[j][i] == "l":
                isAConsumed = True
        if not isAConsumed:
            return False

    return True

def testCore(a: str, b: str) -> None:
    print(isAbbreviation(a, b))

def test1() -> None:
    # Yes
    testCore("daBcd", "ABC")

def test2() -> None:
    # No
    testCore("sYOCa", "YOCN")

def test3() -> None:
    # No
    testCore("KXzQ", "K")

#test1()
#test2()
test3()