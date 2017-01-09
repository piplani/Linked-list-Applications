class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            print str(temp.data) + '->',
            temp = temp.next
        print

    def rotate(self, k):
        temp = self.head
        last = self.head
        c = 0
        ne = temp.next
        while temp:
            ne = temp.next
            c += 1
            if c == k:
                break
            temp = temp.next

        while last.next:
            last = last.next
        temp.next = None
        last.next = self.head

        self.head = ne




if __name__ == '__main__':
    llist1 = LinkedList()
    llist2 = LinkedList()

    llist1.head = Node('rohan')
    second = Node('karan')
    third = Node('shivam')
    fourth = Node('muskaan')
    fifth = Node('ayush')
    sixth = Node('tanya')
    llist1.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    print "Before rotating"
    llist1.printlist()
    print "After rotating"
    llist1.rotate(3)
    llist1.printlist()
