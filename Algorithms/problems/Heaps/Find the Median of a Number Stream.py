# Design a class to calculate the median of a number stream. The class should have the following two methods:

# insertNum(int num): stores the number in the class
# findMedian(): returns the median of all numbers inserted in the class
# If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.

from heapq import *
class findMedianStream:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []
        
    def insertNum(self, num):
        if not self.maxHeap or -self.maxHeap[0] >= num:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)
            
        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.maxHeap) < len(self.minHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))
            
    def findMedian(self):
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0])/2 + (self.minHeap[0])/2
        else:
            return (-self.maxHeap[0])
        
        
stream = findMedianStream()
stream.insertNum(1)
stream.insertNum(3)
stream.insertNum(5)
stream.insertNum(7)

stream.findMedian()