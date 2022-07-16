class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hashmap = {}
        windowStart = 0
        currentSum = 0
        maxSum = 0
        windowStartNew = 0
        for windowEnd in range(len(nums)):
            rightNum = nums[windowEnd]
            if rightNum not in hashmap:
                hashmap[rightNum] = windowEnd
            else:
                windowStartNew = hashmap[rightNum] + 1
                hashmap[rightNum] = windowEnd

            currentSum += rightNum

            while windowStart < windowStartNew:
                leftNum = nums[windowStart]
                currentSum -= leftNum
                windowStart += 1

            maxSum = max(maxSum, currentSum)

        return maxSum