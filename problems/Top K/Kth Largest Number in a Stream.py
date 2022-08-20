# Design a class to efficiently find the Kth largest element in a stream of numbers.

# The class should have the following two things:

# The constructor of the class should accept an integer array containing initial numbers from the stream and an integer ‘K’.
# The class should expose a function add(int num) which will store the given number and return the Kth largest number.
nums = [3, 1, 5, 12, 2, 11]
k = 4

from heapq import *
class kLargestStream:
    def __init__(self, nums, k):
        self.k = k
        self.nums = nums
        self.minHeap = []
        for n in nums:
            self.add(n)
            
    def add(self, value):
        heappush(self.minHeap, value)
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)
            
        return self.minHeap[0]
            
test = kLargestStream(nums, k)
test.add(6)
test.add(13)
test.add(4)