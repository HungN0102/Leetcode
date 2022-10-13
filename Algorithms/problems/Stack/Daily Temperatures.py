# Given an array of integers temperatures represents the daily temperatures, 
# return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
# If there is no future day for which this is possible, keep answer[i] == 0 instead.

class Solution(object):
    def dailyTemperatures(self, temperatures):
        stacks = []
        results = [0 for i in range(len(temperatures))]
        
        for i in range(len(temperatures)):
            while len(stacks) > 0 and temperatures[i] > temperatures[stacks[-1]]:
                resultIndex = stacks.pop()
                results[resultIndex] = i - resultIndex
            stacks.append(i)
            
        return results