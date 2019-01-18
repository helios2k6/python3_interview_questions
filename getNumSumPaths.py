class Node:
    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None

    def __repr__(self):
        return self.value

def processSums(node, totalSums, sideSums):
    if not sideSums:
        return

    for sideSum in sideSums:
        head = sideSum[0]
        newSum = node.value + head
        newSums = [newSum] + sideSum
        totalSums.append(newSums)

def findNumSumPathsImpl(node):
    if not node:
        return []

    if not node.l and not node.r:
        return [[node.value]]

    lSums = findNumSumPathsImpl(node.l)
    rSums = findNumSumPathsImpl(node.r)

    totalSums = []
    processSums(node, totalSums, lSums)
    processSums(node, totalSums, rSums)

    return totalSums

def findNumSumPaths(node, sum):
    allSums = findNumSumPathsImpl(node)
    print(allSums)
    counter = 0
    for sumArray in allSums:
        for iSum in sumArray:
            if iSum == sum:
                counter += 1

    return counter

def test():
    a = Node(1)
    b = Node(2)
    c = Node(3)

    d = Node(1)
    e = Node(-1)
    f = Node(2)
    g = Node(3)

    a.l = b
    a.r = c

    b.l = d
    b.r = e
    
    c.l = f
    c.r = g

    numPaths = findNumSumPaths(a, 3)
    print(f"Num paths (EXPECTED: 2): {numPaths}")

def test2():
    a = Node(1)
    b = Node(2)
    c = Node(3)

    d = Node(1)
    e = Node(-1)
    f = Node(2)
    g = Node(3)

    a.l = b
    a.r = c

    b.l = d
    b.r = e
    
    c.l = f
    c.r = g

    numPaths = findNumSumPaths(a, 2)
    print(f"Num paths (EXPECTED: 2): {numPaths}")

test()