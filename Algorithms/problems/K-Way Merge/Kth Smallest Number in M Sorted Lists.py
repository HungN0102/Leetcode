# Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

L1=[2, 6, 8]
L2=[3, 6, 7]
L3=[1, 3, 4]
K=5

from heapq import *
def kth_smallest_in_m_sorted_lists(lists, k):
    minHeap = []
    for list_ in lists:
        heappush(minHeap, (list_[0], 0, list_))
        
    numberCount = 0
    while minHeap:
        if numberCount == k:
            break 
        
        value, index, list_ = heappop(minHeap)
        if index < len(list_) - 1:
            heappush(minHeap, (list_[index+1], index+1, list_))
        numberCount += 1 
        
    return value 

kth_smallest_in_m_sorted_lists([L1, L2, L3], K)