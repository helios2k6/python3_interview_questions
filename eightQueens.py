def isOnDiag(arr, col, row):
    posM = -col + row
    negM = col + row

    for (i, j) in arr:
        posMij = i - posM
        negMij = -i + negM
        if j == posMij or j == negMij:
            return True
    return False

def r(arrangement, l):
    s = []
    cols = {}
    rows = {}

    for (i, j) in arrangement:
        cols[i] = True
        rows[j] = True

    for i in range(0, l):
        if i in cols:
            continue
        for j in range(0, l):
            if j in rows:
                continue
            if isOnDiag(arrangement, i, j):
                continue
            s.append((i, j))
    return s

def nQueens(n, l):
    if n <= 0:
        return {}
    if n == 1:
        m = []
        for i in range(0, l):
            for j in range(0, l):
                m.append([(i, j)])
        return m

    nMinusOne = nQueens(n - 1, l)
    m = []
    for arrangement in nMinusOne:
        possiblePos = r(arrangement, l)
        for pos in possiblePos:
            c = arrangement.copy()
            c.append(pos)
            m.append(c)
    return m

def test1():
    arrangements = nQueens(3, 4)
    print(arrangements)

test1()