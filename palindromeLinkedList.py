class LinkedListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

def isPalindrome(ll: LinkedListNode):
    turtle = ll
    rabbit = ll
    count = 1 if ll else 0
    while rabbit and rabbit.next:
        turtle = turtle.next
        rabbit = rabbit.next
        count += 1
        if rabbit.next:
            rabbit = rabbit.next
            count += 1

    stackOfNodes = []
    cursor = ll
    while not (cursor is turtle):
        stackOfNodes.append(cursor)
        cursor = cursor.next

    if count % 2 != 0 and count > 1:
        turtle = turtle.next

    for i in reversed(range(len(stackOfNodes))):
        leftSide = stackOfNodes[i].data
        rightSide = turtle.data

        if leftSide != rightSide:
            return False

        turtle = turtle.next

    return True

testA = LinkedListNode(1, None)
test0 = LinkedListNode(1, LinkedListNode(1, None))
test1 = LinkedListNode(1, LinkedListNode(2, LinkedListNode(1, None)))
test2 = LinkedListNode(1, LinkedListNode(2, LinkedListNode(2, LinkedListNode(1, None))))

print(isPalindrome(testA))
print(isPalindrome(test0))
print(isPalindrome(test1))
print(isPalindrome(test2))
