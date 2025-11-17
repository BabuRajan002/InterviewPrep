# 92. Reverse Linked List II

# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
#         dummy = ListNode(0)
#         dummy.next = head

#         leftPre = dummy
#         currNode = head

#         for i in range(left-1):
#             leftPre = leftPre.next
#             currNode = currNode.next
        
#         subListHead = currNode
#         prev = None
#         for j in range(right-left+1):
#             nextnode = currNode.next
#             currNode.next = prev
#             prev = currNode
#             currNode = nextnode
        
#         leftPre.next = prev
#         subListHead.next = currNode

#         return dummy.next


