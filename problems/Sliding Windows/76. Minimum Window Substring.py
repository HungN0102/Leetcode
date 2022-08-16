class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        output = ""
        windowStart = 0
        match = 0
        minLength = float("inf")
        
        hashmap = {}
        for char in t:
            if char not in hashmap:
                hashmap[char] = 0
            hashmap[char] += 1
            
        for windowEnd in range(len(s)):
            rightChar = s[windowEnd]
            if rightChar in hashmap:
                hashmap[rightChar] -= 1
                if hashmap[rightChar] == 0:
                    match += 1
                
            while match == len(hashmap):
                if windowEnd - windowStart + 1 < minLength:
                    output = s[windowStart:windowEnd+1]
                    minLength = len(output)
                    
                leftChar = s[windowStart]
                if leftChar in hashmap:
                    if hashmap[leftChar] == 0:
                        match -= 1
                    hashmap[leftChar] += 1
                windowStart += 1
                    
        return output

