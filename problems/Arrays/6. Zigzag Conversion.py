# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

class Solution:
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        
        res = ""
        for row in range(numRows):
            increment = (numRows-1)*2
            for index in range(row, len(s), increment):
                res += s[index]
                if row != 0 and row != numRows - 1 and index + increment-row*2 < len(s):
                    secondIndex = index + increment-row*2
                    res += s[secondIndex]
                    
        return res