class Solution:
    """
    Input: String (s)
    Output: Integer (Length of the longest palindrome that can be build )
    """
    def longestPalindrome(self, s: str) -> int:
        lenLongestPalindrome = 0

        chars = set()
        for char in s:
            if (char not in chars):
                chars.add(char)
            else:
                # Character can be found in pair
                chars.remove(char)
                lenLongestPalindrome += 2
        
        # Add one additional character for the middle of palindrome, if possible
        if (len(chars) > 0):
            lenLongestPalindrome += 1
        
        return lenLongestPalindrome
        
