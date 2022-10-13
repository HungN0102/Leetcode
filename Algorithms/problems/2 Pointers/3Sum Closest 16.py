class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        minDif = float("inf")
        closestSum = 0

        for i in range(len(nums) - 2):
            targetSum = target - nums[i]

            left = i + 1
            right = len(nums) - 1

            while left < right:
                currentSum = nums[left] + nums[right]
                absDifference = abs(currentSum-targetSum)
                if currentSum == targetSum:
                    return currentSum + nums[i]
                elif currentSum < targetSum:
                    left += 1
                else:
                    right -= 1

                if absDifference < minDif:
                    minDif = absDifference
                    closestSum = currentSum + nums[i]
                    
        return closestSum