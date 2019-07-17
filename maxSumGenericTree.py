class Tree:
    def __init__(self, name):
        self.name = name
        self.neighbors = {}

    def addNeighbor(self, tree: 'Tree', weight: int) -> None:
        self.neighbors[tree.name] = (tree, weight)

    def getNeighbors(self) -> list:
        return self.neighbors.values()

    def __str__(self):
        return self.name

def maxSumPathInTreeImpl(tree: Tree, root: Tree, currentMax: dict) -> int:
    neighborMaxes = []
    for (neighbor, weight) in tree.getNeighbors():
        if neighbor is not root:
            neighborMax = weight + maxSumPathInTreeImpl(neighbor, tree, currentMax)
            neighborMaxes.append(neighborMax)

    if not neighborMaxes:
        # this happens if we reach a node at the end of a traversal
        # so we can terminate this traversal earlys
        return 0

    # Arbitrarily set the first value to a single neighbor. This prevents the corner case where there'
    # only one neighbor
    maxLoopedPathThroughThisNode = neighborMaxes[0]
    for i in range(0, len(neighborMaxes) - 1):
        for j in range(i + 1, len(neighborMaxes)):
            aMax = neighborMaxes[i]
            bMax = neighborMaxes[j]
            maxLoopedPathThroughThisNode = max(aMax + bMax, maxLoopedPathThroughThisNode)
    
    maxPathNotLoopedThroughThisNode = max(neighborMaxes)
    currentMax["MAX"] = max(maxLoopedPathThroughThisNode, maxPathNotLoopedThroughThisNode)

    return maxPathNotLoopedThroughThisNode

def maxSumPathInTree(tree: Tree) -> int:
    maxRef = {"MAX": 0}
    maxSumPathInTreeImpl(tree, tree, maxRef)
    return maxRef["MAX"]

def testCore(allNodes: list, expectedMax: int) -> None:
    for n in allNodes:
        currentMax = maxSumPathInTree(n)
        if currentMax != expectedMax:
            print(f"Unexpected max found for root node as {n}. Expected: {expectedMax} vs Actual: {currentMax} ")
            return

    print("Expected max found for all nodes")

def test0():
    a = Tree("a")
    b = Tree("b")
    c = Tree("c")

    # a <-> b
    a.addNeighbor(b, 1)
    b.addNeighbor(a, 1)

    # b <-> c
    b.addNeighbor(c, 1)
    c.addNeighbor(b, 1)

    testCore([a, b, c], 2)

def test1():
    a = Tree("a")
    b = Tree("b")
    c = Tree("c")
    d = Tree("d")
    e = Tree("e")
    f = Tree("f")

    # a <-> b
    a.addNeighbor(b, 1)
    b.addNeighbor(a, 1)

    # a <-> c
    a.addNeighbor(c, 3)
    c.addNeighbor(a, 3)
    
    # b <-> e
    b.addNeighbor(e, 1)
    e.addNeighbor(b, 1)

    # e <-> f
    e.addNeighbor(f, 6)
    f.addNeighbor(e, 6)

    # b <-> d
    b.addNeighbor(d, 4)
    d.addNeighbor(b, 4)

    testCore([a, b, c, d, e, f], 11)

test0()
test1()