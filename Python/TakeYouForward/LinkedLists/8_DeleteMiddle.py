## Brute Force
# # Definition of singly linked list:
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def deleteMiddle(self, head):
#         if not head or not head.next:
#             return None 
#         n = 0
#         temp = head 
#         while temp:
#             n += 1
#             temp = temp.next 
        
#         res = n // 2
#         temp = head 
#         while temp:
#             res -= 1
#             if res == 0:
#                 middle = temp.next 
#                 temp.next = temp.next.next 
#             temp = temp.next 
#         return head 

# =====================================================================================================================

## Optimized solution

# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def deleteMiddle(self, head):
#         if not head or not head.next:
#             return None 
        
#         slow = head 
#         fast = head.next.next 
#         while fast != None and fast.next != None:
#             slow = slow.next 
#             fast = fast.next.next
        
#         slow.next = slow.next.next 
#         return head 