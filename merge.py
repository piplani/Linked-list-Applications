class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        count = 0
        temp = self.head
        while temp:
            count +=1
            print temp.data,
            temp = temp.next
    def merge(self, head1, head2):
        temp = head1
        while temp.next:
            temp = temp.next
        temp.next = head2
        self.printlist()

if __name__ == '__main__':
    llist1 = LinkedList()
    llist2 = LinkedList()

    llist1.head = Node(1)
    second = Node(2)
    third = Node(3)
    llist1.head.next = second
    second.next = third

    llist2.head = Node(4)
    fifth = Node(5)
    sixth = Node(6)
    llist2.head.next = fifth
    fifth.next = sixth
    print "first linked list"
    llist1.printlist()
    print
    print "second linked list "
    llist2.printlist()
    print
    print "merged linked list "
    llist1.merge(llist1.head, llist2.head)
    print
    llist1.printlist()
