class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printlist(self):
        temp = self.head
        while temp:
            print temp.data
            print temp
            temp = temp.next

    def push(self,prev_node, new_data):
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

if __name__ == '__main__' :
    llist = LinkedList()
    llist.head = Node(1)
    third = Node(3)
    fourth = Node(4)
    llist.head.next = third
    third.next = fourth
    llist.push(llist.head,2)
    llist.printlist()