class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        while True:
            print temp.data,
            temp = temp.next
            if temp == self.head:
                break
if __name__ == '__main__':
    llist1 = LinkedList()
    llist2 = LinkedList()

    llist1.head = Node(5)
    second = Node(6)
    third = Node(3)
    llist1.head.next = second
    second.next = third
    third.next = llist1.head
    llist1.traverse()
