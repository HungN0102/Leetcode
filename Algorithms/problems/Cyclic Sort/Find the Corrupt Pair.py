# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. 
# The array originally contained all the numbers from 1 to ‘n’, 
# but due to a data error, one of the numbers got duplicated which also resulted in one number going missing. 
# Find both these numbers.

nums = [3, 1, 2, 3, 6, 4]

def find_pair(nums):
    outputList = []
    
    i = 0
    while i <= len(nums) - 1:
        if nums[i] != i + 1:
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[j], nums[i] = nums[i], nums[j]
            else:
                i += 1
        else:
            i += 1
    
    for i in range(len(nums)):
        if nums[i] != i + 1:
            outputList.append(nums[i])
            outputList.append(i+1)
    return outputList 

find_pair(nums)