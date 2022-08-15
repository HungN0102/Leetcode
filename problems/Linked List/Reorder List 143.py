# You are given the head of a singly linked-list. The list can be represented as:

# L0 → L1 → … → Ln - 1 → Ln
# Reorder the list to be on the following form:

# L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

class Node:
    def __init__(self, value, next=None):
        self.value = value 
        self.next = next 
        
def reverse(head):
    prev = None
    while head is not None:
        next = head.next 
        head.next = prev 
        prev = head 
        head = next
    return prev
    
def rearrange(head):
    slow = head 
    fast = head 
    while fast is not None and fast.next is not None:
        slow = slow.next 
        fast = fast.next.next
        
    second_half_reversed = reverse(slow)
    first_half = head 
    
    while second_half_reversed is not None and first_half is not None:
        temp = first_half.next
        first_half.next = second_half_reversed
        first_half = temp 
        
        temp = second_half_reversed.next
        second_half_reversed.next = first_half
        second_half_reversed = temp 

    first_half.next = None

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

rearrange(head)

head.value
head.next.value
head.next.next.value
head.next.next.next.value
head.next.next.next.next.value
head.next.next.next.next.next.value
head.next.next.next.next.next.next.value