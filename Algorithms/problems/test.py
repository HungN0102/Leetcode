s = "A man, a plan, a canal: Panama1"
def validP(s):
    alphabets = [character.lower() for character in s if character.isalnum()]
    s = "".join(alphabets)

    left = 0
    right = len(s) - 1
    
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True 

validP(s)