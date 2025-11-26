# 1721. Swapping Nodes in a Linked List

# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
#         curr = head
#         for i in range(k-1):
#             curr = curr.next
        
#         left = curr
#         right = head

#         while curr.next:
#             curr = curr.next
#             right = right.next
        
#         left.val, right.val = right.val, left.val
#         return head


    
        