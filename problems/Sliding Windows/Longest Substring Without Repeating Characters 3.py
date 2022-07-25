class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hashmap = {}
        windowStart = 0
        maxLength = 0
        
        for windowEnd in range(len(s)):
            rightChar = s[windowEnd]
            if rightChar not in hashmap:
                hashmap[rightChar] = 0
            hashmap[rightChar] += 1
            
            while hashmap[rightChar] > 1:
                leftChar = s[windowStart]
                hashmap[leftChar] -= 1
                if hashmap[leftChar] == 0:
                    del hashmap[leftChar]
                
                windowStart += 1
                
            maxLength = max(maxLength, windowEnd - windowStart + 1)
        return maxLength
        