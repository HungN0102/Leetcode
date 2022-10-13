# Given a set of numbers that might contain duplicates, find all of its distinct subsets.

nums = [1, 5, 3, 3]
def solution(nums):
    nums.sort()
    
    subsets = []
    subsets.append([])
    
    for i in range(len(nums)):
        currentNum = nums[i]
        n = len(subsets)
        startIndex = 0 if i > 0 and currentNum != nums[i-1] else int(n/2) 
        for i in range(startIndex, n):
            setCopy = list(subsets[i])
            setCopy.append(currentNum)
            subsets.append(setCopy)
            
    return subsets

solution(nums)