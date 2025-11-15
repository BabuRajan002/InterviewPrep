# # 148. Sort List

# # Given the head of a linked list, return the list after sorting it in ascending order.

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# #Leetcode version

# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None or head.next is None:
#             return head
        
        
#         right = self.getMid(head)
#         tmp = right.next
#         right.next = None
#         right = tmp
#         left = head

#         left = self.sortList(left)
#         right = self.sortList(right)

#         return self.mergeList(left, right)
#     def getMid(self, head):
#         slow, fast = head, head.next
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
#         return slow
    
#     def mergeList(self, list1, list2):
#         tail = dummy = ListNode(0)
        
#         while list1 and list2:
#          if list1.val <= list2.val:
#             tail.next = list1
#             list1 = list1.next
#          else:
#             tail.next = list2
#             list2 = list2.next
#          tail = tail.next
#         if list1:
#             tail.next = list1
#         if list2:
#             tail.next = list2
#         return dummy.next