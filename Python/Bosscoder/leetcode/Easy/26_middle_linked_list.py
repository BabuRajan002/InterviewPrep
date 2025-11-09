# 876. Middle of the Linked List

# Given the head of a singly linked list, return the middle node of the linked list.

# If there are two middle nodes, return the second middle node.

class Node:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
    @staticmethod
    def build_list(nums):
        head = Node(0)
        tail = head
        for num in nums:
            tail.next = Node(num)
            tail = tail.next
        return head.next
    @staticmethod
    def middle_ll(head):
        sp, fp = head, head
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
        return sp.val

if __name__ == "__main__":
    ll = Node.build_list([1,2,3,4,5,6])    
    print(Node.middle_ll(ll))

#Leetcode version
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         sp, fp = head, head
#         while fp and fp.next:
#             sp = sp.next
#             fp = fp.next.next
#         return sp



    

        
