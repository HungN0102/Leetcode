# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

class Solution:
    def isPalindrome(self, s: str) -> bool:
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