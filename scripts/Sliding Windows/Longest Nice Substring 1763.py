class Solution(object):
    def longestNiceSubstring(self, s):
        best = ""
        for windowStart in range(len(s)):
            for windowEnd in range(len(s),windowStart,-1):
                sub = s[windowStart:windowEnd]
                
                originalUniqueLength = len(set(sub))
                lowerUniqueLength = len(set(sub.lower()))
                if lowerUniqueLength*2 == originalUniqueLength:
                    if len(sub) > len(best):
                        best = sub
        return best