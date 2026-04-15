# ## Optimized Approach 

# # Definition of doubly linked list:
# # class ListNode:
# #     def __init__(self, val=0, next=None, prev=None):
# #         self.val = val
# #         self.next = next
# #         self.prev = prev

# class Solution:
#     def deleteAllOccurrences(self, head, target):
#         temp = head 
#         while temp:
#             if temp.val == target:
#                 if temp == head:
#                     head = head.next 
#                 nextNode = temp.next 
#                 prevNode = temp.prev 
#                 if nextNode:
#                     nextNode.prev = prevNode
#                 if prevNode:
#                     prevNode.next = nextNode
#                 temp = temp.next 
#             else:
#                 temp = temp.next 
#         return head 
            

