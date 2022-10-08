class Solution(object):
    def canPartition(self, array):
        total = sum(array)
        if total % 2 != 0 or len(array) <= 1:
            return False 

        target = int(total/2)
        results = [[0 for _ in range(target+1)] for _ in range(len(array))]

        # for any subset, it can make 0
        for index in range(len(array)):
            results[index][0] = True 

        # for the first value, it can make itself or 0
        for t in range(target+1):
            results[0][t] = False
            if t == 0 or t == array[0]:
                results[0][t] = True 

        for index in range(1,len(array)):
            for t in range(target+1):
                results[index][t] = results[index-1][t]
                if not results[index][t] and t-array[index] >= 0:
                    results[index][t] = results[index-1][t-array[index]]

        return results[-1][-1]