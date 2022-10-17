    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = [False for _ in range(len(nums))]
        dp[0] = True
        
        for index in range(len(nums)):
            if index == True:
                for addMe in range(1, nums[index]):
                    dp[index+addMe] = True