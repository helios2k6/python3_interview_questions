class Node:
    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None

def find(node, a):
    if node is a:
        return True

    l = find(node.l, a) if node and node.l else None
    r = find(node.r, a) if node and node.r else None
    return l or r

def fca(node, a, b):
    if node is a:
        return a
    if node is b:
        return b

    aOnLeft = find(node.l, a)
    bOnLeft = find(node.l, b)
    aOnRight = find(node.r, a)
    bOnRight = find(node.r, b)
    if (aOnRight and bOnLeft) or (bOnRight and aOnLeft):
        return node
    if aOnLeft:
        return fca(node.l, a, b)
    else:
        return fca(node.r, a, b)

def test():
    a = Node(1)
    b = Node(2)
    c = Node(3)

    a.l = b
    a.r = c

    common = fca(a, b, c)

    print(f"Common ancestor is {common.value}")

def test2():
    a = Node(1)
    b = Node(2)
    c = Node(3)

    a.l = b
    b.r = c

    common = fca(a, b, c)

    print(f"Common ancestor is {common.value}")

def test3():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)

    a.l = b
    b.r = c
    a.r = d

    common = fca(a, c, d)

    print(f"Common ancestor is {common.value}")

test()
test2()
test3()