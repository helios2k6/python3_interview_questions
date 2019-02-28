class Node:
    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None

    def __repr__(self):
        return self.value

def findNumSumPathsImpl(node):
    if not node:
        return None

    if not node.l and not node.r:
        return ([node.value], [])

    lSums = findNumSumPathsImpl(node.l)
    rSums = findNumSumPathsImpl(node.r)

    currentSums = [node.value]
    otherSums = []

    if lSums:
        for i in lSums[0]:
            currentSums.append(i + node.value)
            otherSums.append(i)
        otherSums = otherSums + lSums[1]

    if rSums:
        for i in rSums[0]:
            currentSums.append(i + node.value)
            otherSums.append(i)
        otherSums = otherSums + rSums[1]

    return (currentSums, otherSums)

def findNumSumPaths(node, sum):
    allSums = findNumSumPathsImpl(node)
    counter = 0
    for i in allSums[0]:
        if i == sum:
            counter += 1
    for i in allSums[1]:
        if i == sum:
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
    print(f"Num paths: {numPaths}")

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
    print(f"Num paths: {numPaths}")

test()
test2()