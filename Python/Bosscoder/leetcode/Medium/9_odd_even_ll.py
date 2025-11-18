# 328. Odd Even Linked List
# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         odd_head = odd = ListNode(0)
#         even_head = even = ListNode(0)

#         count = 1
#         while head:
#             if count % 2 == 1:
#                 odd.next = head
#                 odd = odd.next
#             else:
#                 even.next = head
#                 even = even.next
#             head = head.next
#             count += 1
        
#         even.next = None
#         odd.next = even_head.next
        
#         return odd_head.next
        