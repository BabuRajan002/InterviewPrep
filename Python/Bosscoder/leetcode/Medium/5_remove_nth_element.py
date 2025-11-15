# 19. Remove Nth Node From End of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @staticmethod
    def build_list(nums):
        head = Node(0)
        tail = head
        for v in nums:
            tail.next = Node(v)
            tail = tail.next
        return head.next
    
    @staticmethod
    def reverseOrder(head):
        prev = None
        curr = head
        while curr:
            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode
        return prev
    
    @staticmethod
    def removeNthElement(prev,n):
        count = 1 
        fp,rem = prev,prev
        sp = prev.next
        while sp:
            count += 1
            if count == n:
                fp.next = sp.next
                return rem
            sp = sp.next
            fp = fp.next               

    @staticmethod
    def print_list(rem):
        temp = rem
        while temp:
            print(temp.val, end="->")
            temp = temp.next

if __name__ == "__main__":
    ll = Node.build_list([1,2])
    rev = Node.reverseOrder(ll)
    rem = Node.removeNthElement(rev, 1)
    # final = Node.reverseOrder(rem)
    Node.print_list(rem)

#Leetcode version:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         root = ListNode(0)
#         root.next = head
#         fast = root
#         slow = root

#         for i in range(n+1):
#             fast = fast.next
        
#         while fast:
#             fast = fast.next
#             slow = slow.next
        
#         slow.next = slow.next.next

#         return root.next
        

