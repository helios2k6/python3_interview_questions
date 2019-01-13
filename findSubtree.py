class Node:
    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None

    def __repr__(self):
        return self.value

def compare(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False

    if t1.value != t2.value:
        return False

    return compare(t1.l, t2.l) and compare(t1.r, t2.r)

def findSubtree(t1, t2):
    if not t1 and not t2:
        return True
    if not t1:
        return False

    cmp = compare(t1, t2)
    if cmp:
        return True

    l = findSubtree(t1.l, t2)
    if l:
        return True
    r = findSubtree(t1.r, t2)
    if r:
        return True
    return False

def test1():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")

    a.l = b
    a.r = c
    b.l = d
    b.r = e

    b2 = Node("b")
    d2 = Node("d")
    e2 = Node("e")

    b2.l = d2
    b2.r = e2

    result = findSubtree(a, b2)
    print(f"Expect True: {result}")

def test2():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")

    aa = Node("a")

    bb = Node("b")
    dd = Node("d")
    ee = Node("e")
    
    bb.l = dd
    bb.r = ee

    a.l = b
    a.r = c
    b.l = d
    b.r = e
    d.l = aa
    c.r = bb

    b2 = Node("b")
    d2 = Node("d")
    e2 = Node("e")

    b2.l = d2
    b2.r = e2

    result = findSubtree(a, b2)
    print(f"Expect True: {result}")

def test3():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")

    aa = Node("a")

    bb = Node("b")
    dd = Node("d")
    ee = Node("e")
    
    bb.l = dd
    bb.r = ee

    a.l = b
    a.r = c
    b.l = d
    b.r = e
    d.l = aa

    b2 = Node("b")
    d2 = Node("d")
    e2 = Node("e")

    b2.l = d2
    b2.r = e2

    result = findSubtree(a, b2)
    print(f"Expect False: {result}")

test1()
test2()
test3()