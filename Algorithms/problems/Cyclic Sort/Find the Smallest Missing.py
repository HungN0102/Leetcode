# Given an unsorted array containing numbers, find the smallest missing positive number in it.
nums = [3, -2, 0, 1, 2]

def smallest_missing(nums):
    i = 0
    while i <= len(nums) - 1:
        if nums[i] >= 0 and nums[i] != i + 1:
            j = nums[i] - 1
            if j <= len(nums) - 1 and nums[j] != nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
            else:
                i += 1
        else:
            i += 1
    
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return i+1
    
    return -1

smallest_missing(nums)