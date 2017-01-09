class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self,new_data):
        new_node = Node(new_data)
        temp = self.head
        while(temp.next):
            temp = temp.next
        temp.next = new_node

    def printlist(self):
        temp = self.head
        while temp :
            print temp.data
            temp = temp.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.head  = Node(1)
    llist.append(2)
    llist.printlist()
