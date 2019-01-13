class LinkedListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next
    
    def __repr__(self):
        cursor = self
        computedString = ""
        while cursor:
            if cursor.next:
                computedString = f"{computedString}{cursor.data} -> "
            else:
                computedString = f"{computedString}{cursor.data} -> NULL"
            cursor = cursor.next
        return computedString

def sumLinkedListBigEndian(la, lb):
    if not la:
        if not lb:
            return 0
        else:
            return lb
    elif not lb:
        if not la:
            return 0
        else:
            return la

    stackA = []
    stackB = []

    ca = la
    cb = lb

    while ca or cb:
        if ca:
            stackA.append(ca.data)
            ca = ca.next
        if cb:
            stackB.append(cb.data)
            cb = cb.next

    localResultStack = []
    carry = 0
    while len(stackA) > 0 or len(stackB):
        cavalue = stackA.pop() if len(stackA) > 0 else 0
        cbvalue = stackB.pop() if len(stackB) > 0 else 0

        localSum = cavalue + cbvalue + carry
        if localSum > 10:
            carry = 1
            localSum = localSum % 10
        else:
            carry = 0
        
        localResultStack.append(localSum)

    if carry > 0:
        localResultStack.append(carry)
    
    head = None
    for i in range(len(localResultStack)):
        head = LinkedListNode(localResultStack[i], head)
    return head

def sumLinkedListLittleEndian(la, lb):
    if not la:
        if not lb:
            return 0
        else:
            return lb
    elif not lb:
        if not la:
            return 0
        else:
            return la

    cursorA = la
    cursorB = lb
    carry = 0

    resultList = []
    while cursorA or cursorB:
        currentAVal = cursorA.data if cursorA else 0
        currentBVal = cursorB.data if cursorB else 0

        localSum = currentAVal + currentBVal + carry
        
        if localSum >= 10:
            carry = localSum // 10
            localSum = localSum % 10
        else:
            carry = 0

        resultList.append(localSum)

        if cursorA:
            cursorA = cursorA.next
        if cursorB:
            cursorB = cursorB.next
    if carry > 0:
        resultList.append(carry)

    head = None
    while len(resultList) > 0:
        head = LinkedListNode(resultList.pop(), head)

    return head

listA = LinkedListNode(7, LinkedListNode(1, LinkedListNode(6, None)))
listB = LinkedListNode(5, LinkedListNode(9, LinkedListNode(2, None)))

littleSum = sumLinkedListLittleEndian(listA, listB)

print(littleSum)

listABig = LinkedListNode(6, LinkedListNode(1, LinkedListNode(7, None)))
listBBig = LinkedListNode(2, LinkedListNode(9, LinkedListNode(5, None)))

bigSum = sumLinkedListBigEndian(listABig, listBBig)

print(bigSum)