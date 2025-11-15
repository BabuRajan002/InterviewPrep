# Q19. Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

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
    def print_list(head):
        temp = head
        while(temp):
            print(temp.val, end=" ")
            temp = temp.next  

if __name__ == "__main__":
    swap = Node.build_list([1,2,3,4])
    print(Node.print_list(swap))

#Leetcode version
# class Solution:
#     def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None or head.next is None:
#             return head
#         dummy = ListNode(0)
#         dummy.next = head
#         curr = dummy
#         while curr.next and curr.next.next:
#             fp = curr.next
#             sp = curr.next.next
#             curr.next = sp
#             fp.next = sp.next
#             sp.next = fp
#             curr = curr.next.next
#         return dummy.next
    
        
