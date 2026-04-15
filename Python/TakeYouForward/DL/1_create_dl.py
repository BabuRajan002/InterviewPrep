class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None 

class DoublyLinkedList:
    def __init__(self):
        self.head = None 

    def printDoublyList(self):
        temp = self.head 
        while temp:
            print(temp.data, end=" ")
            if temp.next == None:
                last = temp 
            temp = temp.next
        print()
        print("Backward traversal")
        temp = last 
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev 

if __name__ == "__main__":
    dl = DoublyLinkedList()

    dl.head = Node(10)
    middle = Node(20)
    last = Node(30)

    dl.head.prev = None 
    dl.head.next = middle

    middle.prev = dl.head 
    middle.next = last 

    last.prev = middle
    last.next = None 

    dl.printDoublyList()





             

