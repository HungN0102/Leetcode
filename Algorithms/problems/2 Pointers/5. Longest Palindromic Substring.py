# Given a string s, return the longest palindromic substring in s.
s = "babcd"

class Solution(object):
    def longestPalindrome(self, s):
        longestString = ""
        
        if len(s) <= 1:
            return s
        
        for i in range(len(s)):
            longestString = self.getPalindrome(s, i, i, longestString)

            if i - 1 >= 0 and s[i-1] == s[i]:
                longestString = self.getPalindrome(s, i-1, i, longestString)
                
        return longestString
        
    def getPalindrome(self, s, left, right, longestString):
        while left - 1 >= 0 and right + 1 <= len(s) - 1 and s[left-1] == s[right+1]:
            left -= 1
            right += 1

        if len(s[left:right+1]) > len(longestString):
            return s[left:right+1]
        
        return longestString