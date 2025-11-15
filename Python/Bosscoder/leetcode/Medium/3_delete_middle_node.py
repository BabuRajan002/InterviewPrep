# 2095. Delete the Middle Node of a Linked List

# You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

# The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

# For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.

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
    def findMiddle(head):
        curr = head        
        sp, fp = curr, curr
        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next
        val = sp.val
        return val
    @staticmethod
    def deleteMiddle(head, val):
        temp = head
        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
                break
            temp = temp.next
        return head
    
    @staticmethod
    def print_list(head):
        temp = head
        while(temp):
            print(temp.val, end=" ")
            temp = temp.next



if __name__ == "__main__":
    mnode = Node.build_list([2,1])
    midval = Node.findMiddle(mnode)
    after = Node.deleteMiddle(mnode, midval)
    print(Node.print_list(after))
    
        