# Given an m x n matrix, return all elements of the matrix in spiral order.
class Solution(object):

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        outcomes = []
        
        startRow = 0
        startCol = 0
        endRow = len(matrix)-1
        endCol = len(matrix[0])-1
        
        while startRow <= endRow and startCol <= endCol:
            for c in range(startCol, endCol+1, 1):
                outcomes.append(matrix[startRow][c])
            
            for r in range(startRow+1, endRow+1, 1):
                outcomes.append(matrix[r][endCol])
                
            for c in range(endCol-1, startCol-1,-1):
                if startRow == endRow:
                    break
                outcomes.append(matrix[endRow][c])
            
            for r in range(endRow-1,startRow,-1):
                if startCol == endCol:
                    break
                outcomes.append(matrix[r][startCol])
        
            startRow += 1
            startCol += 1
            endRow -= 1
            endCol -= 1
        
        return outcomes