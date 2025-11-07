# From ChatGPT excercies: 

class Node:
        def __init__(self, val=0, next=None):
                self.node = val
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
        def print_list(head):
               current = head
               while(current):
                      print(current.node, end="->")
                      current = current.next
                
if __name__ == "__main__":
       ll = Node.build_list([3,4,5,6])
       Node.print_list(ll)



        