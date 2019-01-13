class BSTNode:
    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None

    def insert(self, e):
        if e.value <= self.value:
            if not self.l:
                self.l = e
            else:
                self.l.insert(e)
        else:
            if not self.r:
                self.r = e
            else:
                self.r.insert(e)

def getHeight(tree: BSTNode):
    if not tree:
        return 0
    lh = getHeight(tree.l)
    rh = getHeight(tree.r)

    return max(lh, rh) + 1

def isBalanced(tree: BSTNode):
    if not tree:
        return True

    lh = getHeight(tree.l)
    rh = getHeight(tree.r)

    if abs(lh - rh) <= 1:
        return isBalanced(tree.l) and isBalanced(tree.r)

    return False

def test():
    e = BSTNode("e")
    c = BSTNode("c")
    d = BSTNode("d")
    a = BSTNode("a")
    f = BSTNode("f")
    b = BSTNode("b")
    a.l = d
    a.r = f
    d.l = c
    c.l = e
    a.r = f
    f.r = b

    print(f"Is balanced: {isBalanced(a)}")

def test2():
    e = BSTNode("e")
    c = BSTNode("c")
    d = BSTNode("d")
    a = BSTNode("a")
    f = BSTNode("f")
    b = BSTNode("b")

    e.l = c
    e.r = d
    c.l = a
    d.l = f
    d.r = b

    print(f"Is balanced: {isBalanced(a)}")

test()
test2()