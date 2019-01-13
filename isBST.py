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

class R:
    def __init__(self):
        self.min = None
        self.max = None

def updateR(val, r):
    if not r.min:
        r.min = val
    if not r.max:
        r.max = val
    if r.min > val:
        r.min = val
    if r.max < val:
        r.max = val

def valBSTImpl(tree, r):
    if not tree:
        return True
    if not tree.l or tree.l.value <= tree.value:
        if not tree.r or tree.r.value >= tree.value:
            lvalid = valBSTImpl(tree.l, r)
            rvalid = valBSTImpl(tree.r, r)
            updateR(tree.value, r)
            return lvalid and rvalid
    return False

def valBST(tree):
    lmax = R()
    rmin = R()

    lvalid = valBSTImpl(tree.l, lmax)
    rvalid = valBSTImpl(tree.r, rmin)
    if lvalid and rvalid:
        if not lmax.max or lmax.max <= tree.value:
            if not rmin.min or rmin.min >= tree.value:
                return True
    return False

def test():
    a = BSTNode(1)
    b = BSTNode(2)
    c = BSTNode(3)
    d = BSTNode(4)
    e = BSTNode(5)
    f = BSTNode(6)

    c.l = b
    b.l = a
    c.r = d
    d.r = e
    e.r = f

    print(f"Is valid BST? {valBST(c)}")

def test2():
    a = BSTNode(1)
    b = BSTNode(2)
    c = BSTNode(3)
    d = BSTNode(4)

    a.r = c
    b.l = a
    b.r = d

    print(f"Is valid BST? {valBST(b)}")

test()
test2()