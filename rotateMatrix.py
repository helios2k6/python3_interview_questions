def printMat(mat):
    n = len(mat)
    for row in range(n):
        acc = ""
        for col in range(n):
            acc = f"{acc} {mat[row][col]}"
        print(acc)

def getNextCord(coord, n):
    return (n - 1 - coord[1], coord[0])

def getQueue(n):
    queue = []
    for row in range(n):
        for col in range(n):
            queue.append((row, col))
    
    return queue

def get(mat, coord):
    row = coord[0]
    col = coord[1]
    return mat[row][col]

def setVal(mat, coord, value):
    row = coord[0]
    col = coord[1]
    mat[row][col] = value

def rotateMat(mat):
    n = len(mat)
    queue = getQueue(n)
    temp = None
    tempCoord = None
    finishedCoords = {}

    while queue:
        currentCoord = queue.pop() if not tempCoord else tempCoord
        currentVal = get(mat, currentCoord) if not temp else temp

        if currentCoord in finishedCoords:
            temp = None
            tempCoord = None
            continue

        destCoord = getNextCord(currentCoord, n)
        temp = get(mat, destCoord)
        tempCoord = destCoord
        setVal(mat, destCoord, currentVal)
        finishedCoords[currentCoord] = True

def runTestCase(mat):
    rotateMat(mat)
    printMat(mat)
    print()

testCase1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

runTestCase(testCase1)