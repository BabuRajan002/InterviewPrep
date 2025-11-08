# 203. Remove Linked List Elements
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

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
        if not head:
            print("None")
            return
        current = head
        while current:
            print(current.val, end="->") 
            current = current.next

    @staticmethod
    def remove_element(head, value):

        while head and head.val == value:
            head = head.next
        
        temp = head
        while temp and temp.next:
              if temp.next.val == value:
                   temp.next = temp.next.next
              else:
                    temp = temp.next
        return head

if __name__ == "__main__":
    ll = Node.build_list([])
    print("Before deleting")
    Node.print_list(ll)
    after_delete = Node.remove_element(ll,6)
    print("\nAfter remove the element")
    Node.print_list(after_delete)

#Leetcode version
# class Solution:
#     def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         while head and head.val == val:
#             head = head.next
        
#         temp = head
#         while temp and temp.next:
#             if temp.next.val == val:
#                 temp.next = temp.next.next
#             else:
#                 temp = temp.next
#         return head
    