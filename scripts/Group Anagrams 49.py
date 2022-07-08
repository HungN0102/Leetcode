class Solution(object):
    def groupAnagrams(self, strs):
        hashmap = {}
        for word in strs:
            orderedWord = "".join(sorted(word))
            if orderedWord not in hashmap:
                hashmap[orderedWord] = [word]
            else:
                hashmap[orderedWord].append(word)

        output = list(hashmap.values())
        return output