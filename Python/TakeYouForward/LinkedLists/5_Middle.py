class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class Solution:
    def __init__(self, head):
        self.head = head
    
    def middleElement(self):
        slow = self.head 
        fast = self.head.next

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        return slow.data

if __name__ == "__main__":
    ll = Node(10)
    ll.next = Node(20)
    ll.next.next = Node(30)
    ll.next.next.next = Node(40)
    ll.next.next.next.next = Node(50)

    sol = Solution(ll)
    print(sol.middleElement())
