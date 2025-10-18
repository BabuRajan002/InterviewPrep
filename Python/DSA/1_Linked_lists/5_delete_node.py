#Delete a node in a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        newnode = Node(data)
        temp = self.head

        if temp == None:
            self.head = newnode
        else:
            lastnode = self.head
            while lastnode.next != None:
                lastnode = lastnode.next
            lastnode.next = newnode
    
    def delete_node(self, val):
        if self.head.data == val:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next != None:
                if temp.next.data == val:
                    temp.next = temp.next.next
                    break
                else:
                    temp = temp.next       
    
    def print_list(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == "__main__":
    llist = LinkedList()

    llist.add_node(10)
    llist.add_node(20)
    llist.add_node(30)
    llist.add_node(40)
    llist.add_node(50)
    llist.add_node(60)
    llist.add_node(70)
    llist.add_node(80)
    llist.add_node(90)
    llist.add_node(100)
    
    llist.delete_node(20)

    llist.print_list()
            


        