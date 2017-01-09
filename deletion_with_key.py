class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def deleteNode(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None :
            if temp.data == key :
                break
            prev = temp
            temp = temp.next

            if temp is None :
                return
            prev.next = temp.next
            temp = None

    def printlist(self):
        temp = self.head
        while temp:
            print temp.data
            # print temp
            temp = temp.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(3)
    third = Node(3)
    llist.head.next = second
    second.next = third
    llist.deleteNode(3)
    llist.printlist()
