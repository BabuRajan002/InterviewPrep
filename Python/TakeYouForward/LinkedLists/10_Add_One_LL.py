# ## Brute Force Solution 

# # Definition of singly linked list:
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def reverse(self, head):
#         prev = None 
#         temp = head 
#         while temp:
#             front = temp.next 
#             temp.next = prev 
#             prev = temp 
#             temp = front 
#         return prev 
#     def addOne(self, head):
#         head = self.reverse(head)
#         temp = head 
#         carry = 1
#         while temp:
#             temp.val = temp.val + carry 
#             if temp.val < 10:
#                 carry = 0
#                 break
#             else:
#                 carry = 1
#                 temp.val = 0
#             temp = temp.next 
        
#         if carry == 1:
#             newNode = ListNode(1)
#             head = self.reverse(head)
#             newNode.next = head 
#             return newNode 
#         head = self.reverse(head)
#         return head 

## Optimized Solution

# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def addOne(self, head):
#         temp = head
#         carry = self.helper(temp)
#         if carry == 1:
#             newNode = ListNode(1)
#             newNode.next = head 
#             return newNode
#         return head
#     def helper(self, temp):
#         if temp == None:
#             return 1 
#         carry = self.helper(temp.next)
#         temp.val = temp.val + carry 
#         if temp.val < 10:
#             return 0 
#         temp.val = 0 
#         return 1 


    
    