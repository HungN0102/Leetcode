# We are given an array containing n distinct numbers taken from the range 0 to n. 
# Since the array has only n numbers out of the total n+1 numbers, find the missing number.

nums = [4, 0, 3, 1]

def find_missing(nums):
    i = 0
    while i <= len(nums) - 1:
        if nums[i] < len(nums) and nums[i] != i:
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        else:
            i += 1

    for i in range(len(nums)):
        if nums[i] != i:
            return i