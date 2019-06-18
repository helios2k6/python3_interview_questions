class Node:
    def __init__(self, id: str) -> None:
        self.neighbors = []
        self.id = id
    def __str__(self) -> str:
        return self.id
    def addNeighbor(self, neighbor: Node, cost: int) -> None:
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
                distances[neighbor] = costToNeighbor
            # Testing to see if the current cost is creator than the path through this node
            elif currentCostToNeighbor > costToCurrentNode + costToNeighbor:
                distances[neighbor] = costToCurrentNode + costToNeighbor
        visitedNodes[currentNode] = True
        del unvisitedNodes[currentNode]