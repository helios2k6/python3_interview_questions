class Tree:
    def __init__(self, name, value):
        self.l = None
        self.r = None
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name} ({self.value})"

def maxSumPathInTreeImpl(tree: Tree, currentMax: dict) -> int:
    if not tree.l and not tree.r:
        currentMax["MAX"] = max(tree.value, currentMax["MAX"])
        return tree.value

    leftMax = maxSumPathInTreeImpl(tree.l, currentMax) if tree.l else 0
    rightMax = maxSumPathInTreeImpl(tree.r, currentMax) if tree.r else 0

    leftPath = leftMax + tree.value
    rightPath = rightMax + tree.value

    maxPathNonLoopedPath = max(leftPath, rightPath)
    maxLoopedPath = leftMax + tree.value + rightMax

    currentMax["MAX"] = max(max(maxLoopedPath, maxPathNonLoopedPath), currentMax["MAX"])

    return maxPathNonLoopedPath

def maxSumPathInTree(tree: Tree) -> int:
    maxRef = {"MAX": 0}
    maxSumPathInTreeImpl(tree, maxRef)
    return maxRef["MAX"]

def testCore(tree: Tree, expectedSum: int) -> None:
    print(f"Expected: {expectedSum} vs Actual: {maxSumPathInTree(tree)}")

def test0() -> None:
    a = Tree("a", -15)
    # Left
    b = Tree("b", 5)
    c = Tree("c", -8)
    d = Tree("d", 2)
    e = Tree("e", 6)
    f = Tree("f", 1)
    b.l = c
    b.r = f
    c.l = d
    c.r = e

    # Right
    g = Tree("g", 6)
    h = Tree("h", 3)
    i = Tree("i", 9)
    j = Tree("j", 0)
    k = Tree("k", 4)
    l = Tree("l", -1)
    m = Tree("m", 10)
    g.l = h
    g.r = i
    i.r = j
    j.l = k
    j.r = l
    l.l = m

    a.l = b
    a.r = g

    testCore(a, 27)

test0()