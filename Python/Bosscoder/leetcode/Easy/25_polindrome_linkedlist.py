# Q26. Palindrome Linked List

# Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    @staticmethod
    def build_list(vals):
        head = Node(0)
        tail = head
        for v in vals:
            tail.next = Node(v)
            tail = tail.next
        return head.next
        
    @staticmethod
    def divide_list(head):
        if head is None or head.next is None:
            return True
        sp, fp = head, head
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next        
        
        p2 = Node.reverse_order(sp)

        p1 = head
        
        while p2:
         if p1.val != p2.val:
            return False
         p1 = p1.next
         p2 = p2.next
        return True

    @staticmethod
    def reverse_order(head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev 

if __name__ == "__main__":
    ll = Node.build_list([1,2,2,3])
    print("Is Polindrome?:", Node.divide_list(ll))


#Leetcode version


# class Solution:
#     def reverse_order(self,head):
#         prev = None
#         curr = head
#         while curr:
#             nextnode = curr.next
#             curr.next = prev
#             prev = curr
#             curr = nextnode

#         return prev
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         if head is None and head.next is None:
#             return True
#         sp, fp = head, head
#         while fp and fp.next:
#             sp = sp.next
#             fp = fp.next.next

#         p2 = self.reverse_order(sp)

#         p1 = head

#         while p2:
#             if p1.val != p2.val:
#                 return False
#             p1 = p1.next
#             p2 = p2.next
#         return True       