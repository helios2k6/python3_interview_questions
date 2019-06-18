class Node:
    def __init__(self, id: str) -> None:
        self.neighbors = []
        self.id = id
    def __str__(self) -> str:
        return self.id
    def addNeighbor(self, neighbor: "Node", cost: int) -> None:
        self.neighbors.append((neighbor, cost))

def chooseNextNode(distances: dict, unvisitedNodes: dict) -> Node:
    if not unvisitedNodes:
        return None

    chosenNode = None
    chosenNodeDistance = None
    for node, distance in distances.items():
        if node in unvisitedNodes:
            if not chosenNode or chosenNodeDistance > distance:
                chosenNode = node
                chosenNodeDistance = distance
    return chosenNode

def dijkstra(nodes: list, start: Node, end: Node) -> list:
    distances = { start: 0 }
    visitedNodes = {}
    unvisitedNodes = {}
    previousNodes = {}
    for n in nodes:
        unvisitedNodes[n] = True

    currentNode = start
    while unvisitedNodes:
        if end in visitedNodes:
            break
        if currentNode in visitedNodes:
            currentNode = chooseNextNode(distances, unvisitedNodes)
        costToCurrentNode = distances[currentNode]
        for neighborAndCost in currentNode.neighbors:
            neighbor = neighborAndCost[0]
            costToNeighbor = neighborAndCost[1]
            currentCostToNeighbor = distances[neighbor] if neighbor in distances else None
            # Testing for effectively "infinity"
            if not currentCostToNeighbor:
                distances[neighbor] = costToNeighbor + distances[currentNode]
                previousNodes[neighbor] = currentNode
            # Testing to see if the current cost is creator than the path through this node
            elif currentCostToNeighbor > costToCurrentNode + costToNeighbor:
                distances[neighbor] = costToCurrentNode + costToNeighbor
                previousNodes[neighbor] = currentNode
        visitedNodes[currentNode] = True
        del unvisitedNodes[currentNode]

    trackingNode = end
    path = []
    while trackingNode:
        path.append(trackingNode)
        if trackingNode in previousNodes:
            trackingNode = previousNodes[trackingNode]
        else:
            trackingNode = None
    return reversed(path)

def testCore(nodes: list, start: Node, end: Node) -> None:
    path = dijkstra(nodes, start, end)
    strings = []
    for node in path:
        strings.append(node.__str__())
        strings.append(" -> ")

    print("".join(strings[0:-1]))

def test0() -> None:
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")

    # graph setup:
    # a -> b: 5
    # a -> c: 2
    # b -> d: 1
    # c -> e: 6
    # d -> e: 3
    # path from a -> e should be: a -> c -> e
    a.addNeighbor(b, 5)
    a.addNeighbor(c, 2)
    b.addNeighbor(d, 1)
    c.addNeighbor(e, 6)
    d.addNeighbor(e, 3)

    testCore([a, b, c, d, e,], a, e)

test0()