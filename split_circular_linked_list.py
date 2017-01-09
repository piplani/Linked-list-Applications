class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        c = 0
        while True:
            print temp.data,
            c += 1
            temp = temp.next
            if temp == self.head:
                print
                return c

    def append(self, new_data):

        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)

        # 4. If the Linked List is empty, then make the
        #    new node as head
        if self.head is None:
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next

        # 6. Change the next of last node
        last.next = new_node

    def make_it_circular(self):
        temp = self.head
        while temp.next:
            temp = temp.next
        temp = self.head

    def printlist(self):
        count = 0
        temp = self.head
        while temp:
            count +=1
            print temp.data,
            temp = temp.next





    def split(self):
        print "linked list"
        c = self.traverse()
        x = 1
        temp = self.head
        l1 = LinkedList()
        l2 = LinkedList()
        while True:
            if x <= c/2:
                l1.append(temp.data)
            else:
                l2.append(temp.data)
            temp = temp.next
            x+=1
            if temp == self.head:
                break
        #l1.make_it_circular()
        #l2.make_it_circular()
        print "first half"
        l1.printlist()
        print
        print "second half"
        l2.printlist()





if __name__ == '__main__':
    llist1 = LinkedList()
    llist2 = LinkedList()

    llist1.head = Node(12)
    second = Node(56)
    third = Node(2)
    fourth = Node(11)
    llist1.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = llist1.head
    llist1.split()
