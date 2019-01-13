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

    def __repr__(self):
        return self.value

def weave(a, b):
    if not a:
        return [b]
    if not b:
        return [a]
    aHead = a[0]
    aTail = a[1:]
    bHead = b[0]
    bTail = b[1:]

    results = []
    tookAPerms = weave(aTail, b)
    tookBPerms = weave(bTail, a)

    for aPerm in tookAPerms:
        results.append([aHead] + aPerm)

    for bPerm in tookBPerms:
        results.append([bHead] + bPerm)

    return results

def seq(root):
    if not root:
        return [[]]

    l = seq(root.l)
    r = seq(root.r)

    results = []

    for lCombo in l:
        for rCombo in r:
            weaved = weave(lCombo, rCombo)
        for w in weaved:
            results.append([root.value] + w)

    return results

def test():
    a = BSTNode(5)
    b = BSTNode(0)
    c = BSTNode(10)
    d = BSTNode(-5)
    e = BSTNode(3)
    f = BSTNode(7)

    a.l = b
    a.r = c
    b.l = d
    b.r = e
    c.l = f

    results = seq(a)
    print(results)

test()