# We are given an unsorted array containing numbers taken from the range 1 to ‘n’. 
# The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

nums = [2, 3, 1, 8, 2, 3, 5, 1]

def find_all_missing(nums):
    outputList = []
    i = 0
    while i <= len(nums) -1:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1
            
    for i in range(len(nums)):
        if i + 1 != nums[i]:
            outputList.append(i+1)
            
    return outputList