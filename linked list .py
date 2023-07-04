class Node:                           # created a node whenever the instance  of node class is created
    def __init__(self, value=None):   # if we do not give any value to the value then it will take none
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):           #MAGIC METHOD to go to the next node of the linked list
        node = self.head
        while node:
            yield node            # yield used
            node = node.next      # next node
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail=newNode


singlyLinkedList = SLinkedList()    # instance of SlinkedList is created
singlyLinkedList.insertSLL(1,0)
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 0)
singlyLinkedList.insertSLL(4, 1)
singlyLinkedList.insertSLL(5,-1)


print([node.value for node in singlyLinkedList])
