# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

class Solution(object):
    def trap(self, height):
        maxLeft = 0
        maxRight = 0
        totalWater = 0

        left = 0
        right = len(height) - 1
        while left < right:
            maxLeft = max(maxLeft, height[left])
            maxRight = max(maxRight, height[right])

            if maxLeft < maxRight:
                left += 1
                totalWater += max(min(maxLeft, maxRight) - height[left],0)
            else:
                right -= 1
                totalWater += max(min(maxLeft, maxRight) - height[right],0)
        return totalWater
    