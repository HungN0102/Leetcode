from heapq import *
import heapq
def maxSlidingWindow(nums, k):
    maxHeap = []
    results = [0 for _ in range(len(nums)-k+1)]
    
    for i in range(len(nums)):
        heappush(maxHeap, -nums[i])
        if i >= k - 1:
            results[i-k+1] = -maxHeap[0]
            removeElement(maxHeap, -nums[i-k+1])
    return results

def removeElement(maxHeap, element):
    indexToRemove = maxHeap.index(element)
    maxHeap[indexToRemove] = maxHeap[-1]
    del maxHeap[-1]
    if indexToRemove < len(maxHeap):
        heapq._siftup(maxHeap, indexToRemove)
        heapq._siftdown(maxHeap, 0, indexToRemove)
    
maxSlidingWindow([5,4,3,2,1],2)