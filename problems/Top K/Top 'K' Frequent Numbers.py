# Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.
nums = [1, 3, 5, 12, 11, 12, 11]
k = 2

from heapq import *
def solution(nums, k):
    hashmap = {}
    for n in nums:
        if n not in hashmap:
            hashmap[n] = 0
        hashmap[n] += 1
        
    minHeap = []
    for key, freq in hashmap.items():
        heappush(minHeap, [freq, key])
        
    while len(minHeap) > k:
        heappop(minHeap)
        
    return [element[1] for element in minHeap] 

solution(nums, k)