class Solution(object):
    def sortedSquares(self, nums):
        holderList = [0 for i in range(len(nums))]
        left = 0
        right = len(nums) - 1
        i = len(nums) - 1
        while left <= right:
            leftNum = nums[left]**2
            rightNum = nums[right]**2
            if leftNum > rightNum:
                holderList[i] = leftNum
                left += 1
            else:    
                holderList[i] = rightNum
                right -= 1
            i -= 1
        return holderList