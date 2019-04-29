class Node:
    def __init__(self, value):
        self.edges = []
        self.value = value

    def addEdge(self, neighbor, weight):
        self.edges.append((neighbor, weight))

def maxSumWithNode(node):
    sums = []
    for (neighbor, weight) in node.edges:
        sums.append(maxSumWithoutNodeImpl(neighbor, node, 0) + weight)
    if not sums:
        return 0
    if len(sums) == 1:
        return sums[0]
    sums.sort(reverse=True)
    return sums[0] + sums[1]

def maxSumWithoutNodeImpl(node, parent, runningValue):
    currentMaxValue = runningValue
    for (neighbor, weight) in node.edges:
        if neighbor is not parent:
            localMax = maxSumWithoutNodeImpl(neighbor, node, runningValue + weight)
            if currentMaxValue < localMax:
                currentMaxValue = localMax
    return currentMaxValue

def maxSumWithoutNode(node):
    return maxSumWithoutNodeImpl(node, None, 0)

def maxPath(node):
    return max(maxSumWithNode(node), maxSumWithoutNode(node))

def testImpl(nodes):
    for node in nodes:
        print(f"Testing with node {node.value}: {maxPath(node)}")

def test1():
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")

    a.addEdge(b, 1)
    b.addEdge(a, 1)

    b.addEdge(c, 10)
    c.addEdge(b, 10)

    b.addEdge(d, 20)
    d.addEdge(b, 20)

    # Choose b because it's the crappiest root
    #testImpl([a, b, c, d])
    print(f"{maxSumWithNode(a)} vs {maxSumWithoutNode(a)}")

test1()