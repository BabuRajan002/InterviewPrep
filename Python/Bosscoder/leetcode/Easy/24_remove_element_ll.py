# 203. Remove Linked List Elements
# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

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
    def print_list(head):
        current = head
        while current:
            print(current.val, end="->") 
            current = current.next

    @staticmethod
    def remove_element(head, value):
        if head.val == value:
            head = head.next
        else:
            temp = head
            while temp.next != None:
                if temp.next.val == value:
                    temp.next = temp.next.next
                else:
                    temp = temp.next
        return temp.next

    # def delete_node(self, val):
    #     if self.head.data == val:
    #         self.head = self.head.next
    #     else:
    #         temp = self.head
    #         while temp.next != None:
    #             if temp.next.data == val:
    #                 temp.next = temp.next.next
    #                 break
    #             else:
    #                 temp = temp.next 

if __name__ == "__main__":
    ll = Node.build_list([1,2,3,4,5,6])
    print("Before deleting")
    Node.print_list(ll)
    after_delete = Node.remove_element(ll,5)
    print("After remove the element")
    Node.print_list(after_delete)
    