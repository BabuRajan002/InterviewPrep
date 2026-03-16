class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
    

class Solution:
    def __init__(self, head, key):
        self.head = head
        self.key = key 
    
    def solve(self):
        temp = self.head
        while temp:
            if temp.data == self.key:
                return True 
            temp = temp.next 
        return False 

if __name__ == "__main__":
    ll = Node(10)
    ll.next = Node(20)
    ll.next.next = Node(30)
    ll.next.next.next = Node(40)

    sol = Solution(ll, 30)
    print(sol.solve())

    
