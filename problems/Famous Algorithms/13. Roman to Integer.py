class Solution(object):
    def romanToInt(self, s):
        hashmap = {   "I": 1,
                        "V": 5,
                        "X": 10,
                        "L": 50,
                        "C": 100,
                        "D": 500,
                        "M": 1000}
        
        total = 0
        i = 0
        while i <= len(s) - 1:
            if i + 1 <= len(s) - 1 and hashmap[s[i]] < hashmap[s[i+1]]:
                total += hashmap[s[i+1]] - hashmap[s[i]]
                i += 2
            else:
                total += hashmap[s[i]]
                i += 1
        
        return total
        