class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Hold head of the linkedlist
class LinkedList:
    def __init__(self):
        self.head = None

#Printing the linkedList    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next

if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(10)
    middle = Node(20)
    last = Node(30)
    llist.head.next = middle
    middle.next = last
    llist.printList()
