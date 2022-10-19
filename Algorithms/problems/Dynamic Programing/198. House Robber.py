class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        results = [0 for _ in range(len(nums))]
        results[0] = nums[0]
        results[1] = nums[1]
        
        for index in range(2,len(nums)):
            results[index] = results[index-2] + nums[index]
            if index >= 3:
                results[index] = max(results[index], results[index-3]+nums[index])
                
        return max(results)