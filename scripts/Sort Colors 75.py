class Solution(object):
    def sortColors(self, nums):
        low = 0
        high = len(nums) - 1
        i = 0
        while i <= high and low <= high:
            value = nums[i]
            if value == 1 :
                i += 1
            elif value == 0 and low <= high:
                nums[low], nums[i] = nums[i], nums[low]
                i += 1
                low += 1
            elif value == 2 and low <= high:
                nums[high], nums[i] = nums[i], nums[high]
                high -= 1
        return nums