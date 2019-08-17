def minStringEditDistance(a: str, b: str) -> int:
    numEdits = [[0 for _ in range(0, len(b) + 1)] for _ in range(0, len(a) + 1)]
    for i in range(0, len(a)):
        for j in range(0, len(b)):
            if not numEdits[i][j]:
                if i < j or j > i:
                    numEdits[i][j] = numEdits[i - 1][j - 1] + 1
                elif i == j:
                    if i < len(a) and j < len(b) and a[i] != b[j]:
                        numEdits[i][j] = numEdits[i - 1][j - 1] + 1

    return numEdits[len(a)][len(b)]

def testCore(a: str, b: str) -> None:
    print(minStringEditDistance(a, b))

def test1() -> None:
    testCore("a", "ab")

def test2() -> None:
    testCore("geek", "geesk")

test1()
test2()