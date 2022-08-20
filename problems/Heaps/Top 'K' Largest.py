# Given an unsorted array of numbers, find the ‘K’ largest numbers in it
nums = [3, 1, 5, 12, 2, 11]
k = 3

from heapq import *
def solution(nums, k):
    minHeap = []
    for i in range(k):
        heappush(minHeap, nums[i])
        
    for i in range(k, len(nums)):
        if nums[i] > minHeap[0]:
            heappop(minHeap)
            heappush(minHeap, nums[i])
            
    return minHeap 

solution(nums, k)