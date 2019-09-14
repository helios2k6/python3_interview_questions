def minStringEditDistance(a: str, b: str) -> int:
    numEdits = [[0 for _ in range(0, len(b) + 1)] for _ in range(0, len(a) + 1)]

    # Initialize zeros
    for i in range(0, len(b) + 1):
        numEdits[0][i] = i
    for i in range(0, len(a) + 1):
        numEdits[i][0] = i

    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            prevValue = min(numEdits[i - 1][j], numEdits[i][j - 1], numEdits[i - 1][j - 1])
            if a[i - 1] == b[j - 1]:
                numEdits[i][j] = prevValue
            else:
                numEdits[i][j] = prevValue + 1

    return numEdits[len(a)][len(b)]

def testCore(a: str, b: str) -> None:
    print(minStringEditDistance(a, b))

def test1() -> None:
    testCore("a", "ab")

def test2() -> None:
    testCore("geek", "geesk")

def test3() -> None:
    testCore("andrewjohnson", "andyni")

test1()
test2()
test3()