# We are given an unsorted array containing n numbers taken from the range 1 to n. 
# The array has some numbers appearing twice, find all these duplicate numbers using constant space.
nums = [3, 4, 4, 5, 5]

def find_all_duplicates(nums):
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
        if nums[i] != i +1:
            outputList.append(nums[i])
    
    return outputList


find_all_duplicates(nums)