# Exercise 4: Traverse Backward (Without Doubly Linked List)

# 🎯 Goal

# Print the linked list in reverse order — but without modifying it or using a doubly linked list.
# You must use recursion.

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
        while current:
            print(current.val, end="->")
            current = current.next

    @staticmethod
    def reverse_order(head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev 

if __name__ == "__main__":
    ll = Node.build_list([1,2,3])
    print("Original Linked List:")
    Node.print_list(ll)
    reversed_list = Node.reverse_order(ll)
    print("Reversed LinkedList")
    Node.print_list(reversed_list)