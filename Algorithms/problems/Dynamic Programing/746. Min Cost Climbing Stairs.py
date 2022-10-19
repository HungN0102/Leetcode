class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        results = [0 for _ in range(len(cost)+1)]
        
        for index in range(2,len(cost)+1):
            results[index] = min(cost[index-1]+results[index-1], cost[index-2]+results[index-2])
            
        return results[-1]