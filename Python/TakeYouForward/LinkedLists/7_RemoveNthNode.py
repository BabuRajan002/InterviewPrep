## Brute Force Approach
# # Definition for Singly Linked List
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def removeNthFromEnd(self, head, n):
#         temp = head
#         count = 0
#         while temp:
#             count += 1
#             temp = temp.next 
        
#         if count == n:
#             newHead = head.next 
#             return newHead
        
#         res = count - n 
#         temp = head 
#         while temp:
#             res -= 1

#             if res == 0:
#                 break 
#             else:
#                 temp = temp.next 
        
#         dnode = temp.next 
#         temp.next = temp.next.next
#         return head 
        
        