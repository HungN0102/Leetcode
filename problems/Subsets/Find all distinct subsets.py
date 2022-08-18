# Given a set with distinct elements, find all of its distinct subsets.
nums = [1, 3, 3]
def solution(nums):
    subsets = []
    subsets.append([])
    
    for currentNum in nums:
        n = len(subsets)
        for i in range(n):
            setCopy = list(subsets[i])
            setCopy.append(currentNum)
            subsets.append(setCopy)
            
    return subsets