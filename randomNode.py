import random

class Node:
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None

class Tree:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, node):
        self.count += 1
        if not self.root:
            self.root = node
            return

        self.insertImpl(self.root, node)

    def insertImpl(self, currentNode, externalNode):
        if not currentNode.l:
            currentNode.l = externalNode
        elif not currentNode.r:
            currentNode.r = externalNode
        else:
            s = random.randint(0, 1)
            if s == 0:
                self.insertImpl(currentNode.l, externalNode)
            else:
                self.insertImpl(currentNode.r, externalNode)

    def find(self, val):
        return self.findImpl(self.root, val)

    def findImpl(self, currentNode, val):
        if not currentNode:
            return None
        if currentNode.val is val or currentNode.val == val:
            return currentNode
        
        lResult = self.findImpl(currentNode.l, val)
        if lResult:
            return lResult
        return self.findImpl(currentNode.r, val)

    def findParentImpl(self, currentNode, node):
        if not currentNode:
            return None
        if currentNode.l is node or currentNode.r is node:
            return currentNode

        lResult = self.findParentImpl(currentNode.l, node)
        if lResult:
            return lResult
        return self.findParentImpl(currentNode.r, node)

    def findSuitableNodeImpl(self, currentNode, parentNode):
        if not currentNode:
            return None

        if not currentNode.l and not currentNode.r:
            if parentNode:
                if parentNode.l is currentNode:
                    parentNode.l = None
                else:
                    parentNode.r = None
                return currentNode

        if currentNode.l:
            return self.findSuitableNodeImpl(currentNode.l, currentNode)
        else:
            return self.findSuitableNodeImpl(currentNode.r, currentNode)

    def delete(self, node):
        self.count -= 1
        parent = self.findParentImpl(self.root, node) if not self.root is node else None
        bottomReplacement = self.findSuitableNodeImpl(node, parent)
        if bottomReplacement:
            bottomReplacement.l = node.l
            bottomReplacement.r = node.r

        if parent:
            if parent.l is node:
                parent.l = bottomReplacement
            else:
                parent.r = bottomReplacement

    def getNodesInListImpl(self, node, acc):
        if not node:
            return

        acc.append(node)
        self.getNodesInListImpl(node.l, acc)
        self.getNodesInListImpl(node.r, acc)


    def getRandomNode(self):
        listOfNodes = []
        self.getNodesInListImpl(self.root, listOfNodes)
        return listOfNodes[random.randint(0, self.count - 1)]
