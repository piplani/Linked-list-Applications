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

    def swap(self,x, y):
        prevX = None
        prevY = None
        currX = self.head
        currY = self.head
        # finding prev and curr node with data x
        while currX:
            if currX.data == x:
                break
            prevX = currX
            currX = currX.next
        # finding prev and curr node with data y
        while currY:
            if currY.data == y:
                break
            prevY = currY
            currY = currY.next
        # checking whether currX is not head
        if prevX is not None:
            prevX.next = currY # linking prevX with currY
        else:
            self.head = currY # making currY as head if currX is head
        # checking whether currY is not head
        if prevY is not None:
            prevY.next = currX # linking prevY with currX
        else:
            self.head = currX # making currX as head if currY is head
        # swapping pointers stored in node
        temp = currX.next
        currX.next = currY.next
        currY.next = temp

if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)

    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth

    llist.swap(3, 4)
    llist.printlist()

