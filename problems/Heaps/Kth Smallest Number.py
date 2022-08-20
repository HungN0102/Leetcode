# Given an unsorted array of numbers, find Kth smallest number in it.

# Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

nums = [1, 5, 12, 2, 11, 5]
k = 3

from heapq import *
def solution(nums, k):
    maxHeap = []
    for i in range(k):
        heappush(maxHeap, -nums[i])
        
    for i in range(k, len(nums)):
        if nums[i] < -maxHeap[0]:
            heappop(maxHeap)
            heappush(maxHeap, -nums[i])
            
    return -maxHeap[0]

solution(nums, k)