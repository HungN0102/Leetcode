# Given an unsorted array of integers nums. 
# Return the start/ end index of the longest consecutive elements sequence.

array = [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]

def largestRange(array):
    nums = {}
    for num in array:
        nums[num] = True
        
    outputList = [0, 0]
    outputLength = 0
    for num in array:
        if not nums[num]:
            continue 
        nums[num] = False
        currentLength = 1
        left = num - 1
        right = num + 1
        while left in nums:
            nums[left] = False
            currentLength += 1
            left -= 1
        while right in nums:
            nums[right] = False
            currentLength += 1
            right += 1
        if currentLength > outputLength:
            outputLength = currentLength
            outputList = [left+1, right - 1]
    
    return outputList 

largestRange(array)
