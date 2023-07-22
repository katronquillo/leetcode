class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome, longestLength = "", 0

        # Find the longest palindrome with the current char as "middle"
        for i in range(len(s)):
            # Looking for odd length palindromes (I.E. Mirrored excluding curr char)
            left, right = i, i
            while (0 <= left and right < len(s) and s[left] == s[right]):
                currLength = (right - left) + 1
                if (currLength > longestLength):
                    longestLength = currLength
                    palindrome = s[left:right + 1]
                left -= 1
                right += 1
            
            # Looking for even length palindromes (I.E. Mirror including curr char)
            left, right = i, i + 1
            while (0 <= left and right < len(s) and s[left] == s[right]):
                currLength = (right - left) + 1
                if (currLength > longestLength):
                    longestLength = currLength
                    palindrome = s[left:right + 1]
                left -= 1
                right += 1

        return palindrome
        