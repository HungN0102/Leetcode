# Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost. 
# The cost of connecting two ropes is equal to the sum of their lengths.

nums = [1, 3, 11, 5]

from heapq import *
def solution(nums):
    totalCost = 0
    
    minHeap = []
    for n in nums:
        heappush(minHeap, n)
        
    while len(minHeap) != 1:
        smallest = heappop(minHeap)
        secondSmallest = heappop(minHeap)
        
        cost = smallest + secondSmallest
        heappush(minHeap, cost)
        
        totalCost += cost 
        
    return totalCost 

solution(nums)