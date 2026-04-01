# ## Brute Force Solution:
# # # Definition of singly linked list:
# # # class ListNode:
# # #     def __init__(self, val=0, next=None):
# # #         self.val = val
# # #         self.next = next

# # class Solution:
# #     def sortList(self, head):
# #         temp = head 
# #         arr = []
# #         while temp:
# #             arr.append(temp.val)
# #             temp = temp.next 
# #         nums = self.arrSort(arr)
# #         temp = head 
# #         i = 0
# #         while temp:
# #             temp.val = nums[i]
# #             temp = temp.next 
# #             i += 1
# #         return head  

    
# #     def arrSort(self, arr):
# #         n = len(arr)
# #         for i in range(n):
# #             for j in range(i+1, n):
# #                 if arr[j] < arr[i]:
# #                     temp = arr[j]
# #                     arr[j] = arr[i]
# #                     arr[i] = temp
# #         return arr 
    
 
# # Definition of singly linked list:
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# # Definition of singly linked list:
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def sortList(self, head):
#         if not head or not head.next: 
#             return head  
        
#         middle = self.findMiddle(head)
#         left = head 
#         right = middle.next 
#         middle.next = None

#         left = self.sortList(left)
#         right = self.sortList(right) 

#         return self.mergeTwoSortedLinkedLists(left, right)

    
#     def findMiddle(self, head):
#         if not head or head.next:
#             return head 

#         slow = head 
#         fast = head.next 
#         while fast and fast.next:
#             slow = slow.next 
#             fast = fast.next.next 
#         return slow
    
#     def mergeTwoSortedLinkedLists(self, list1, list2):
#         dummyNode = ListNode(-1)
#         temp = dummyNode

#         while list1 and list2:
#             if list1.val <= list2.val:
#                 temp.next = list1 
#                 list1 = list1.next 
#             else:
#                 temp.next = list2 
#                 list2 = list2.next 
#             temp = temp.next 
        
#         if list1:
#             temp.next = list1
#         else:
#             temp.next = list2 
#         return dummyNode.next 