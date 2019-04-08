def visit(adjList, visitedNodes, l, node):
    if node in visitedNodes:
        return
    visitedNodes[node] = True
    for neighbor in adjList[node]:
        visit(adjList, visitedNodes, l, neighbor)
    l.append(node)

def transposeAdjList(adjList):
    transposedAdjList = {}
    for node, neighbors in adjList.items():
        for neighbor in neighbors:
            if neighbor in transposedAdjList:
                if node not in transposedAdjList[neighbor]:
                    transposedAdjList[neighbor].append(node)
            else:
                transposedAdjList[neighbor] = [node]
    return transposedAdjList

def hasNodeBeenAssignedToComponent(components, node):
    for root, componentMembers in components.items():
        if node == root or node in componentMembers:
            return True
    return False

def assign(transposedAdjList, components, node, root):
    if hasNodeBeenAssignedToComponent(components, node):
        return
    if root not in components:
        components[root] = []

    componentMembers = components[root]
    componentMembers.append(node)

    for inMember in transposedAdjList[node]:
        assign(transposedAdjList, components, inMember, root)

def stronglyConnectedComponents(adjList):
    visitedNodes = {}
    l = []

    for node, _ in adjList.items():
        visit(adjList, visitedNodes, l, node)

    transposedAdjList = transposeAdjList(adjList)
    components = {}
    for u in reversed(l): #we have to reverse this because we were supposed to prepend stuff, but that's slow in python
        assign(transposedAdjList, components, u, u)
    return components

def test(adjList):
    components = stronglyConnectedComponents(adjList)
    for root, componentMembers in components.items():
        print(f"({root}) -> {componentMembers}")

def test1():
    adjList = {0: [1, 3], 1: [2], 2: [], 3: [4], 4: [0]}
    test(adjList)

test1()