class GraphNode:
    def __init__(self, value):
        self.value = value
        self.edges = []
    
    def addEdge(self, edge):
        self.edges.append(edge)

    def addEdges(self, edges: list):
        for e in edges:
            self.edges.append(e)

    def isEdge(self, edge):
        for e in self.edges:
            if e is edge:
                return True
        return False

class Graph:
    def __init__(self):
        self.nodes = []
    
    def addNode(self, node):
        self.nodes.append(node)


def dequeue(queue: list):
    if queue:
        e = queue[0]
        del queue[0]
        return e
    return None

def processNode(node: GraphNode, seenMap, queue, comparisonNode: GraphNode):
    if node and not (node in seenMap):
        seenMap[node] = True
        if node is comparisonNode:
            return True
        for edge in node.edges:
            queue.append(edge)
    return False

def detectRoute(g1: GraphNode, g2: GraphNode):
    g1Queue = []
    g2Queue = []

    g1Queue.append(g1)
    g2Queue.append(g2)

    seenG1 = {}
    seenG2 = {}

    g1PathFound = False
    g2PathFound = False
    while g1Queue or g2Queue:
        g1Node = dequeue(g1Queue)
        g2Node = dequeue(g2Queue)

        g1ProcessResult = processNode(g1Node, seenG1, g1Queue, g2)
        g2ProcessResult = processNode(g2Node, seenG2, g2Queue, g1)

        g1PathFound = g1ProcessResult if g1ProcessResult else g1PathFound
        g2PathFound = g2ProcessResult if g2ProcessResult else g2PathFound

        if g1PathFound and g2PathFound:
            return True
    return False

def test():
    a = GraphNode(1)
    b = GraphNode(2)
    c = GraphNode(3)
    d = GraphNode(4)
    e = GraphNode(5)

    a.addEdges([b, c])
    b.addEdges([c, e])
    c.addEdge(e)
    d.addEdges([e, c])
    e.addEdges([a, d])

    print(f"Route detected? {detectRoute(a, d)}")

test()