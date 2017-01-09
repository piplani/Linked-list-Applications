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

    def push(self, new_data):

        # 1 & 2: Allocate the Node &
        #        Put in the data
        new_node = Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

    def addtwo(self, head1, head2):
        c = 0
        temp1 = head1
        temp2 = head2
        number1 = 0
        number2 = 0
        while temp1:
            number1 += temp1.data * pow(10, c)
            c += 1
            temp1 = temp1.next
        c = 0
        while temp2:
            number2 += temp2.data * pow(10, c)
            c += 1
            temp2 = temp2.next
        print number1
        print number2
        n3 = number1 + number2
        print n3
        res = LinkedList()
        for i in str(n3):
            res.push(i)
        res.printlist()

if __name__ == '__main__':
    llist1 = LinkedList()
    llist2 = LinkedList()

    llist1.head = Node(5)
    second = Node(6)
    third = Node(3)
    llist1.head.next = second
    second.next = third

    llist2.head = Node(8)
    fifth = Node(4)
    sixth = Node(2)
    llist2.head.next = fifth
    fifth.next = sixth
    llist1.printlist()
    llist2.printlist()
    llist1.addtwo(llist1.head, llist2.head)