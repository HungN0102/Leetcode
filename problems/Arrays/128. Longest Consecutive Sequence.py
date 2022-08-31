# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

nums = [100,4,200,1,3,2]

def longest_consecutive(nums):
    longestStreak = 0
    
    for num in nums:
        if num - 1 not in nums:
            currentStreak = 1
            currentNum = num
            while currentNum + 1 in nums:
                currentStreak += 1
                currentNum += 1
            longestStreak = max(longestStreak, currentStreak)
            
    return longestStreak 

longest_consecutive(nums)