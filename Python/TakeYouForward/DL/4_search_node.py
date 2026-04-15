class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data 
        self.next = None 

class CreateDoubleLL:
    def __init__(self):
        self.head = None 
    
    def createLL(self, val):
        newNode = Node(val)

        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head 
            self.head.prev = newNode
            self.head = newNode
    
    def printDl(self):
        temp = self.head 

        while temp:
            print(temp.data, end="->")
            temp = temp.next 
    
    def searchKey(self, key):

        temp = self.head 
        while temp:
            if temp.data == key:
                return True
            temp = temp.next 
        return False 

if __name__ == "__main__":
    dl = CreateDoubleLL()

    # dl.head = Node(5)
    dl.createLL(10)
    dl.createLL(20)
    dl.createLL(30)
    dl.printDl()
    print()
    print(dl.searchKey(40))



