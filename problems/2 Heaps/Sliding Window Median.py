# Given an array of numbers and a number ‘k’, 
# find the median of all the ‘k’ sized sub-arrays (or windows) of the array.
from heapq import *

class slidingWindowMedian:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        
    def balanceHeap(self):
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
            
    def removeElement(self, heap, element):
        index = heap.index(element)
        heap[index] = heap[-1]
        heap.pop()
        heap = heapify(heap)
        
    def findMedian(self,nums, k):
        result = [0 for i in range(len(nums)-k+1)]
        
        for i in range(len(nums)):
            if not self.maxHeap or -self.maxHeap[0] >= nums[i]:
                heappush(self.maxHeap, -nums[i])
            else:
                heappush(self.minHeap, nums[i])
                
            self.balanceHeap()
            
            if i >= k -1:
                if len(self.maxHeap) == len(self.minHeap):
                    result[i-k+1] = -self.maxHeap[0]/2 + self.minHeap[0]/2
                else:
                    result[i-k+1] = -self.maxHeap[0]
            
                elementToRemove = nums[i-k+1]
                if elementToRemove <= -self.maxHeap[0]:
                    self.removeElement(self.maxHeap, -elementToRemove)
                else:
                    self.removeElement(self.minHeap, elementToRemove)
                
            self.balanceHeap()
            
        return result