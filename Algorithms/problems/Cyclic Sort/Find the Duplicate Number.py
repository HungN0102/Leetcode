# We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. 
# The array has only one duplicate but it can be repeated multiple times. 
# Find that duplicate number without using any extra space. 
# You are, however, allowed to modify the input array.

nums = [2, 4, 1, 3, 4]

def find_single_duplicate(nums):
    i = 0
    while i <= len(nums) - 1:
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:    
                nums[j], nums[i] = nums[i], nums[j]
            else:
                return nums[i]
        else:
            i += 1
    return -1        
        
find_single_duplicate(nums)