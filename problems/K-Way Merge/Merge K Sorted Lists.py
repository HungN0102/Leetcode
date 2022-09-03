# Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

class ListNode:
    def __init__(self, value, next=None):
        self.value = value 
        self.next = next
        
    def __lt__(self, other):
        return self.value < other.value
    
from heapq import *    
def merge_k_sorted_list(lists):
    sorted_list = []
    minHeap = []
    
    for head in lists:
        if head is not None:
            heappush(minHeap, head)
            
    while minHeap:
        currentSmallest = heappop(minHeap)
        sorted_list.append(currentSmallest)
        
        if currentSmallest.next is not None:
            heappush(minHeap, currentSmallest.next)
    
    return [x.value for x in sorted_list]

l1 = ListNode(2)
l1.next = ListNode(6)
l1.next.next = ListNode(8)

l2 = ListNode(3)
l2.next = ListNode(6)
l2.next.next = ListNode(7)

l3 = ListNode(1)
l3.next = ListNode(3)
l3.next.next = ListNode(4) 

merge_k_sorted_list([l1,l2,l3])