class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Algorithm...
        - Use two pointers to iterate string from beginning and end
        - Shift pointers forward until reaching alphanumeric characters
        - Compare alphanumeric characters at both pointers
            - If they don't match, then not a palindrome 
        - Continue until pointers meet in the middle 
        """
        left, right = 0, len(s) - 1
        while (left <= right and left < len(s) and right >= 0):
            if (not s[left].isalnum()):
                left += 1
                continue
            
            if (not s[right].isalnum()):
                right -= 1
                continue
            
            if (s[left].lower() != s[right].lower()):
                return False
            
            left += 1
            right -= 1

        return True
        