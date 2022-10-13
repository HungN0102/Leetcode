class Solution(object):
    def fourSum(self, nums, target):
        output = []
        nums.sort()
        
        for i in range(len(nums)-3):
            if i - 1 >= 0 and nums[i] == nums[i-1]:
                continue
                
            for j in range(i+1, len(nums)-2):
                if j - 1 >= i + 1 and nums[j] == nums[j-1]:
                    continue
                targetSum = target - nums[i] - nums[j]
                
                leftIndex = j+1
                rightIndex = len(nums) - 1
                
                while leftIndex < rightIndex:
                    currentTotal = nums[leftIndex] + nums[rightIndex]
                    
                    if currentTotal == targetSum:
                        output.append([nums[i], nums[j], nums[leftIndex], nums[rightIndex]])
                        leftIndex += 1
                        rightIndex -= 1
                        while leftIndex < rightIndex and nums[leftIndex] == nums[leftIndex-1]:
                            leftIndex += 1
                        while leftIndex < rightIndex and nums[rightIndex] == nums[rightIndex+1]:
                            rightIndex -= 1
                    elif currentTotal < targetSum:
                        leftIndex += 1
                    else:
                        rightIndex -= 1
                        
        return output