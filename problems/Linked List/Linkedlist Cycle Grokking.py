# Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.

class Node:
    def __init__(self, data, next=None):
        self.data = data 
        self.next = next
        
        
def has_cycle(head):
    slow = head 
    fast = head 
    while slow is not None and fast is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False    

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    return str(has_cycle(head))
    
main()