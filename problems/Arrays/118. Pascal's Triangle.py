# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

numRows = 5
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = [[1]]
        if numRows == 1:
            return pascal

        for _ in range(1,numRows):
            newRow = self.createRow(pascal[-1])
            pascal.append(newRow)

        return pascal
    
    def createRow(self, previousRow):
        results = [0 for i in range(len(previousRow)+1)]
        for i in range(len(previousRow)+1):
            if i == 0 or i == len(previousRow):
                results[i] = 1
                continue

            results[i] = previousRow[i] + previousRow[i-1]

        return results 