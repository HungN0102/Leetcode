# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.

from collections import deque
class Solution(object):
    def minRemoveToMakeValid(self, s):
        openStack = []
        notTakeIndex = []

        for i in range(len(s)):
            if s[i] not in "()":
                continue
            elif s[i] == "(":
                openStack.append(i)
            elif not openStack:
                notTakeIndex.append(i)
            else:
                openStack.pop()

        notTakeIndex += openStack
        notTakeIndex.sort()

        level = 0
        outputString = ""
        for i in range(len(s)):
            if level <= len(notTakeIndex) - 1 and i == notTakeIndex[level]:
                level += 1
            else:
                outputString += s[i]

        return outputString
