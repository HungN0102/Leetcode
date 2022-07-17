class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        left = 0
        product = 1
        count = 0
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k and left <= right:
                product /= nums[left]
                left += 1
            
            count += right - left + 1
        return count