class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 

class Solution:
    def __init__(self, head):
        self.head = head 
    
    def solve(self):
        count = 0
        temp = self.head 
        while temp:
            temp = temp.next 
            count += 1
        return count 

if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    

    sol = Solution(head)
    print(sol.solve())
        