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
            print temp.data
            temp = temp.next

        return count

if __name__ == '__main__':
    llist = LinkedList()

    llist.head = Node(10)
    second = Node(20)
    third = Node(30)

    llist.head.next = second
    second.next = third

    c = llist.printlist()
    print c

