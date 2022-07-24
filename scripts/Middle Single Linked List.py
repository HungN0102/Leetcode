class Node:
    def __init__(self, value, next=None):
        self.value = value 
        self.next = next
        
def middle_linked_list(node):
    slow = node 
    fast = node 
    while fast is not None and fast.next is not None:
        slow = slow.next 
        fast = fast.next.next 
    return slow 

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)

    print("Middle Node: " + str(middle_linked_list(head).value))
    
main()