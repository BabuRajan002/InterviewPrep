# # # From chatGPT:
# # Goal:
# # Build the linked list dynamically from user input instead of a predefined list.
# 🧠 Problem Statement
# Write a program that:
# Takes numbers as input from the user (space-separated).
# Builds a linked list from those numbers.
# Prints the linked list in forward order.

class Node:
        def __init__(self, val=0, next=None):
                self.node = val
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
               while(current):
                      print(current.node, end="->")
                      current = current.next
                
if __name__ == "__main__":
     numbers = input("Enter the numbers with some spaces:").split(" ")    
     vals = []
     for num in numbers:
            vals.append(int(num))
     
     ll = Node.build_list(vals)
     Node.print_list(ll)
            
            
