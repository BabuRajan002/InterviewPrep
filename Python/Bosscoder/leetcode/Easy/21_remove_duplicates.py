# 83. Remove Duplicates from Sorted List

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Definition for singly-linked list.
# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Build a linked list from a Python list
    @staticmethod #Using this we can call this method directly from the class
    def build_list(vals):
        head = ListNode(0)  # dummy node
        tail = head
        for v in vals:
            tail.next = ListNode(v)
            tail = tail.next
        return head.next  # skip dummy node


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return res


# ---------- main block ----------
if __name__ == "__main__":
    # Build a linked list from a Python list
    head = ListNode.build_list([1, 1, 2, 3, 3])
    
    # Call the solution
    head = Solution().deleteDuplicates(head)
    
    # Convert the linked list back to Python list for easy printing
    out = []
    while head:
        out.append(head.val)
        head = head.next

    print(out)  # Output: [1, 2, 3]

    # #Leetcode version:
    # class Solution:
    # def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     res = head
    #     while head and head.next:
    #         if head.val == head.next.val:
    #             head.next = head.next.next
    #         else:
    #             head = head.next
        
    #     return res
