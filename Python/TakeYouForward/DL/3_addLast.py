class Node:
    def __init__(self, data):
        self.prev = None 
        self.data = data
        self.next = None 

class CreateDoubleLL:
    def __init__(self):
        self.head = None  
    
    def addLast(self, val):
        newNode = Node(val)

        if self.head == None:
            self.head = newNode
        else:
            last = self.head 

            while last.next:
                last = last.next 
            
            last.next = newNode
            newNode.prev = last 
    
    def printDl(self):
        temp = self.head 

        while temp:
            print(temp.data, end=" ")
            temp = temp.next 

if __name__ == "__main__":
    dl = CreateDoubleLL()

    dl.head = Node(10)

    dl.addLast(20)
    dl.printDl()

