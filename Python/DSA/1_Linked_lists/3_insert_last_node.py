# Inserting a node at the end of the linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def addLast(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
        else:
            lastNode = self.head

            while(lastNode.next):
                lastNode = lastNode.next
            
            lastNode.next = new_node
    
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == "__main__":
    llist = LinkedList()

    print("adding a last element:")
    llist.addLast(10)

    print("adding a last element:")
    llist.addLast(20)

    llist.print_list()


        