nums = [999,999,999,999]

def largest_area(nums):
    largestArea = 0
    for i in range(len(nums)):
        width = 1
        height = nums[i]
        
        leftIndex = i - 1
        while leftIndex >= 0 and nums[leftIndex] >= nums[i]:
            width += 1
            leftIndex -= 1
        
        rightIndex = i + 1
        while rightIndex <= len(nums) - 1 and nums[rightIndex] >= nums[i]:
            width += 1
            rightIndex += 1
        
        largestArea = max(largestArea, width*height)
    return largestArea 

largest_area(nums)            

