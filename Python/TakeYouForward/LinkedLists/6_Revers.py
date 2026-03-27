class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None
    
class Solution:
    def __init__(self, head):
        self.head = head 
    
    def solve(self):
        temp = self.head 
        prev = None 

        while temp:
            front = temp.next 
            temp.next = prev 
            prev = temp 
            temp = front 
        return prev == self.head
    
    def printList(self, prev):
        temp = prev 
        while temp:
            print(temp.data, end="->")
            temp = temp.next    

if __name__ == "__main__":
    ll = Node(10)
    ll.next = Node(20)
    ll.next.next = Node(30)
    ll.next.next.next = Node(40)

    sol = Solution(ll)
    rev = sol.solve()
    sol.printList(rev)