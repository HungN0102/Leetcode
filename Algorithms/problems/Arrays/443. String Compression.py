class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """   
        i = 0
        replaceIdx = 0
        while i <= len(chars) - 1:
            count = 1
            while i + 1 <= len(chars) - 1 and chars[i] == chars[i+1]:
                count += 1
                i += 1

            chars[replaceIdx] = chars[i]
            replaceIdx += 1
            if count != 1:
                countString = str(count)
                for cString in countString:
                    chars[replaceIdx] = cString
                    replaceIdx += 1

            i += 1
        return replaceIdx