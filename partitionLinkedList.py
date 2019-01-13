class LinkedListNode:
    def __init__(self, data, next):
        self.data = data
        self.next = next

def partition(linkedList, partition):
    head = linkedList
    previousNode = linkedList
    cursor = linkedList.next
    while cursor:
        if cursor.data < partition:
            previousNode.next = cursor.next
            cursor.next = head
            head = cursor
            cursor = previousNode.next
        else:
            previousNode = previousNode.next
            cursor = cursor.next

    return head

linkedList = LinkedListNode(3, LinkedListNode(5, LinkedListNode(8, LinkedListNode(5, LinkedListNode(10, LinkedListNode(2, LinkedListNode(1, None)))))))

partitionedLinkedList = partition(linkedList, 5)

cursor = partitionedLinkedList
computedString = ""
while cursor:
    computedString = f"{computedString}{cursor.data} -> "
    cursor = cursor.next

print(computedString)