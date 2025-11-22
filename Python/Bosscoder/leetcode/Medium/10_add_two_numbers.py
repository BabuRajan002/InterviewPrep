# 2. Add Two Numbers

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def build_list(self, nums):
        head = Node(0)
        tail = head
        for num in nums:
            tail.next = Node(num)
            tail = tail.next        
        return head.next
    
    def build_list1(self, nums):
        head1 = Node(0)
        tail1 = head1
        for num in nums:
            tail1.next = Node(num)
            tail1 = tail1.next        
        return head1.next
    
    def print_list(self, head):
        temp = head
        while temp:
            print(temp.val, end=",")
            temp = temp.next
        print()
    
    def addTwoNumbers(self, head, head1):
        temp = head
        temp1 = head1
        carry = 0
        add_head = Node(0)
        temp_head = add_head
        while temp or temp1 or carry:
            val1 = temp.val if temp else 0 
            val2 = temp1.val if temp1 else 0

            
            sum = val1 + val2 + carry
            carry = sum // 10
            digit = sum % 10

            temp_head.next = Node(digit)
            temp_head = temp_head.next

            if temp:
                temp = temp.next
            if temp1:
                temp1 = temp1.next
        return add_head.next


if __name__ == "__main__":
    ll = Node()    
    ll1 = ll.build_list([9,9,9,9,9,9,9])
    ll2 = ll.build_list1([9,9,9,9])
    llsum = ll.addTwoNumbers(ll1, ll2)

    ll.print_list(ll1)
    ll.print_list(ll2)
    ll.print_list(llsum)

# #Leetcode:

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

#         temp1 = l1
#         temp2 = l2
#         carry = 0
#         sum_head = ListNode(0)
#         temp_head = sum_head

#         while temp1 or temp2 or carry:
#             val1 = temp1.val if temp1 else 0
#             val2 = temp2.val if temp2 else 0 

#             sum = val1 + val2 + carry

#             carry = sum // 10
#             digit = sum % 10

#             temp_head.next = ListNode(digit)
#             temp_head = temp_head.next

#             if temp1:
#                 temp1 = temp1.next
            
#             if temp2:
#                 temp2 = temp2.next
#         return sum_head.next