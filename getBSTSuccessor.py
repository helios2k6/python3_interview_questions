class BSTNode:
    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None
        self.parent = None

    def insert(self, e):
        if e.value <= self.value:
            if not self.l:
                self.l = e
                e.parent = self
            else:
                self.l.insert(e)
        else:
            if not self.r:
                self.r = e
                e.parent = self
            else:
                self.r.insert(e)

def getSuccessor(tree):
    # check for right child
    if tree.r:
        # cycle through all left children
        currentNode = tree.r
        while currentNode.l:
            currentNode = currentNode.l
        return currentNode
    else:
        if not tree.parent:
            return None
        else:
            # check to see which child we are
            if tree.parent.l is tree:
                # we are the left child. Return the parent
                return tree.parent
            else:
                currentNode = tree
                parentNode = tree.parent
                while parentNode and not parentNode.l is currentNode:
                    currentNode = parentNode
                    parentNode = parentNode.parent
                return parentNode

def test():
    a = BSTNode(3)
    b = BSTNode(1)
    c = BSTNode(0)
    d = BSTNode(2)
    e = BSTNode(7)
    f = BSTNode(5)
    g = BSTNode(4)
    h = BSTNode(6)
    i = BSTNode(8)

    a.l = b
    b.parent = a

    b.l = c
    c.parent = b

    b.r = d
    d.parent = b

    a.r = e
    e.parent = a

    e.l = f
    f.parent = e

    f.l = g
    g.parent = f

    f.r = h
    h.parent = f

    e.r = i
    i.parent = e

    print(f"{getSuccessor(i)}")

test()