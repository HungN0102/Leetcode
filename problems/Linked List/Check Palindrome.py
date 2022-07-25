# Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next 
    

def reverse(node):
    prev = None
    while node is not None:
        next = node.next 
        node.next = prev 
        prev = node 
        node = next 
    return prev

def palindrome(head):
    if head is None or head.next is None:
        return False 
    
    slow = head 
    fast = head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

    head_second_half_reversed = reverse(head)
    check_node = head 
    while check_node is not None and head_second_half_reversed is not None:
        if check_node.value != head_second_half_reversed.value:
            return False 
        check_node = check_node.next 
        head_second_half_reversed = head_second_half_reversed.next
    return True
    
head = Node(2)
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(4)
head.next.next.next.next = Node(2)

palindrome(head)