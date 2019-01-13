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

class BST:
    def __init__(self):
        self.root = None

    def insert(self, e):
        if not self.root:
            self.root = BSTNode(e)
        else:
            self.root.insert(BSTNode(e))

    def getListRepresentation(self, node, level, ll):
        if not node:
            return

        if len(ll) - 1 < level:
            row = [node.value]
            ll.append(row)
        else:
            ll[level].append(node.value)

        self.getListRepresentation(node.l, level + 1, ll)
        self.getListRepresentation(node.r, level + 1, ll)


    def __repr__(self):
        outputList = []
        self.getListRepresentation(self.root, 0, outputList)
        stringBuilder = ""
        level = 0
        for nodes in outputList:
            if level > 0:
                stringBuilder = f"{stringBuilder}\n"
            stringBuilder = f"{stringBuilder}{level}:"
            for node in nodes:
                stringBuilder = f"{stringBuilder} {node}"
            level += 1

        return stringBuilder

def createBST(l, upper, lower, tree):
    if upper - lower == 0:
        return

    pivot = ((upper - lower) // 2) + lower
    tree.insert(l[pivot])
    createBST(l, pivot, lower, tree) # left
    createBST(l, upper, pivot + 1, tree) # right

def test():
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    tree = BST()
    createBST(l, 10, 0, tree)
    print(tree)

test()