# Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.

# If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()
            

def reverse_every_k_linkedlist(head,k):
    if head is None or head.next is None or k <= 1:
        return head
    
    current = head
    prev = None
    while True:
        last_in_sub = current
        last_before_sub = prev
        
        i = 0
        while current is not None and i < k:
            next = current.next 
            current.next = prev 
            prev = current 
            current = next 
            i += 1
            
        if last_before_sub is not None:
            last_before_sub.next = prev 
        else:
            head = prev 
            
        last_in_sub.next = current 
        
        if current is None:
            break 
        
        prev = last_in_sub  
    return head




head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

head = reverse_every_k_linkedlist(head,3)

head.print_list()