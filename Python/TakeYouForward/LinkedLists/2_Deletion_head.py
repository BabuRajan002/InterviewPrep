class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None

class Solution:
    def __init__(self, head):
        self.head = head 
    
    def solve(self):
        if self.head is None or self.head.next is None:
            return None 
        self.head = self.head.next 
        return self.head 
    
    def printList(self):
        temp = self.head 
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


if __name__ == "__main__":
    head = Node(20)
    head.next = Node(30)
    head.next.next = Node(40)
    head.next.next.next = Node(50)

    sol = Solution(head)
    print("Before")
    sol.printList()
    print()
    sol.solve()
    print("after")
    sol.printList()
