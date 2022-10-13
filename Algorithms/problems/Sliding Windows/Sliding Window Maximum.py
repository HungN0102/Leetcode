# You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. 
# You can only see the k numbers in the window. Each time the sliding window moves right by one position.

# Return the max sliding window.
from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        results = [0 for _ in range(len(nums) - k + 1)]
        maxQ = deque()
        
        windowStart = 0
        windowEnd = 0
        for windowEnd in range(len(nums)):
            while maxQ and nums[maxQ[-1]] <= nums[windowEnd]:
                maxQ.pop()
            maxQ.append(windowEnd)
            
            if windowEnd >= k - 1:
                results[windowStart] = nums[maxQ[0]]
                windowStart += 1 
                
            if maxQ[0] < windowStart:
                maxQ.popleft()
                
        return results