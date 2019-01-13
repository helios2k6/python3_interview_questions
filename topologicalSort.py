class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

    def addNeighbor(self, node):
        self.neighbors.append(node)

    def __repr__(self):
        return self.val

def topologicalSortImpl(node, sortedNodes, permMarks, tempMarks):
    if node in permMarks:
        return

    if node in tempMarks:
        raise RuntimeError("DAG has cycle")

    tempMarks.append(node)
    for neighbor in node.neighbors:
        topologicalSortImpl(neighbor, sortedNodes, permMarks, tempMarks)

    permMarks.append(node)
    sortedNodes.append(node)

def topologicalSort(nodes):
    unmarkedNodes = []
    for n in nodes:
        unmarkedNodes.append(n)

    sortedNodes = []
    permMarks = []
    tempMarks = []
    while unmarkedNodes:
        unmarkedNode = unmarkedNodes.pop()
        topologicalSortImpl(unmarkedNode, sortedNodes, permMarks, tempMarks)

    return reversed(sortedNodes)

def test():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.addNeighbor(d)
    f.addNeighbor(b)
    b.addNeighbor(d)
    f.addNeighbor(a)
    d.addNeighbor(c)

    topSort = topologicalSort([a, b, c, d, e, f])
    for n in topSort:
        print(n)

test()