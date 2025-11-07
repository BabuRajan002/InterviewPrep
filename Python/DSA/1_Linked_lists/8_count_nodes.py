# Exercise 3: Count Number of Nodes in the Linked List

# 🎯 Goal

# Write a method to count the number of nodes in a linked list and display the count.

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @staticmethod
    def build_list(vals):
        head = Node(0)
        tail = head
        for v in vals:
            tail.next = Node(v)
            tail = tail.next
        return head.next
    
    @staticmethod
    def print_list(head):
        current = head
        count = 0
        while (current):
            # print(current.val, end="->")
            current = current.next
            count += 1
        return count

if __name__ == "__main__":
    ll = Node.build_list([6,4,3,2,1])
    print(Node.print_list(ll))

            
