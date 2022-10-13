# Given the head of a LinkedList and two positions ‘p’ and ‘q’. 
# Reverse the LinkedList from position ‘p’ to ‘q’.

from __future__ import print_function
from audioop import reverse
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value)
            temp = temp.next 
        print()
        
def reverse_sub(head, p, q):
    if p == q:
        return head 
    
    prev = None 
    current = head 
    i = 0
    while current is not None and i < p - 1:
        prev = current 
        current = current.next 
        i += 1
        
    last_before = prev 
    last_in_sub = current 
    
    i = 0
    while current is not None and i < q - p + 1:
        next = current.next 
        current.next = prev 
        prev = current 
        current = next 
        i += 1
    
    if last_before is not None:
        last_before.next = prev 
    else:
        head = prev 
    
    last_in_sub.next = current 
    
    return head

head = Node(2)   
head.next = Node(4)
head.next.next = Node(6)
head.next.next.next = Node(8)
head.next.next.next.next = Node(10)
reverse_sub(head, 2, 4)

head.print_list()