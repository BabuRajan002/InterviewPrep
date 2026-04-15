class Node:
    def __init__(self, data):
        self.prev = None 
        self.data = data 
        self.next = None 
    
class CreateDoubleLL:
    def __init__(self):
        self.head = None 
    
    def addFirst(self, val):
        newNode = Node(val)

        if self.head == None: 
            self.head = newNode
        else:
            newNode.prev = None 
            newNode.next = self.head 
            self.head.prev = newNode
            self.head = newNode
    
    def printDl(self):
        temp = self.head 

        while temp:
            print(temp.data, end=" ")
            if temp.next == None:
                last = temp 
            temp = temp.next 
        print()
        print("Bakward traversal")
        temp = last 
        while temp:
            print(temp.data, end=" ")
            temp = temp.prev 

if __name__ == "__main__":
    dl = CreateDoubleLL()

    dl.head = Node(20)
    dl.addFirst(10)
    dl.addFirst(5)

    dl.printDl()











