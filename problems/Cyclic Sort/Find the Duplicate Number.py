nums = [2, 4, 1, 4, 4]

def find_single_duplicate(nums):
    for i in range(len(nums)):
        index = abs(nums[i]) -1
        if nums[index] < 0:
            return abs(nums[index])
        nums[index] *= -1
        
find_single_duplicate(nums)