# In this code we are going to insert a node at the begining:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def print_list(self):
        temp = self.head

        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == "__main__":
    llist = LinkedList()

    
    print("Inserting element: 10")
    llist.add_first(10)

    print("Inserting Element: 20")
    llist.add_first(20)

    print("Inserting element: 30")
    llist.add_first(30)
    
    llist.print_list()




