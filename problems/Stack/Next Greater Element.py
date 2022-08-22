# Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), 
# return the next greater number for every element in nums.

# The next greater number of a number x is the first greater number to its traversing-order next in the array, 
# which means you could search circularly to find its next greater number. 
# If it doesn't exist, return -1 for this number.
nums = [2, 5, -3, -4, 6, 7, 2]

def solution(nums):
    result = [-1 for i in range(len(nums))]
    stack = []
    
    for circularIdx in range(len(nums)*2):
        currentIdx = circularIdx % len(nums)
        currentValue = nums[currentIdx]
        while len(stack) > 0 and currentValue > nums[stack[-1]]:
            indexResult = stack.pop()
            result[indexResult] = currentValue        
        stack.append(currentIdx)
        
    return result 

solution(nums)
