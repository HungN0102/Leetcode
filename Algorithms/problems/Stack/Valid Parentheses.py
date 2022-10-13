# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

def solution(s):
    
    hashmap = {
        "}":"{",
        ")":"(",
        "]":"["
    }
    stack = []
    
    for i in range(len(s)):
        char = s[i]
        if char not in hashmap:
            stack.append(s[i])
        
        if char in hashmap:
            if len(stack) == 0:
                return False 
            
            lastOpen = stack.pop()
            if lastOpen != hashmap[char]:
                print(lastOpen)
                return False 
    return not stack

s = "()[{}]["
solution(s)