class Solution(object):
    def findLength(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        maxResult = 0
        results = [[0 for _ in range(len(nums1))] for _ in range(len(nums2))]
        for r in range(len(nums2)-1,-1,-1):
            for c in range(len(nums1)-1,-1,-1):
                if nums1[c] == nums2[r]:
                    results[r][c] = 1
                    if r + 1 < len(nums2) and c + 1 < len(nums1):
                        results[r][c] += results[r+1][c+1]
                    maxResult = max(maxResult, results[r][c])
        return maxResult