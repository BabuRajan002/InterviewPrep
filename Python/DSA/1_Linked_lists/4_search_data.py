# Search a given Key in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def add_data(self, data):
        new_node = Node(data)
        temp = self.head

        if temp == None:
            self.head = new_node
        else:
            lastnode = self.head
            while(lastnode.next):
                lastnode = lastnode.next
            lastnode.next = new_node
    
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

    def search_data(self, val):
        temp = self.head

        while temp != None: 
            if temp.data == val:
                return True
            temp = temp.next
        return False

if __name__ == "__main__":
    llist = LinkedList()

    llist.add_data(10)
    llist.add_data(20)
    llist.add_data(30)
    print(llist.search_data(60))
    

    
