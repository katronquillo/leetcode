class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        windowStart, windowEnd = 0, 0 
        maxLength = 0
        chars = set()

        for windowEnd in range(len(s)):
            currChar = s[windowEnd]
            if (currChar not in chars):
                chars.add(currChar)
                windowLength = (windowEnd - windowStart) + 1
                maxLength = max(maxLength, windowLength)
            else:
                while (windowStart <= windowEnd and currChar in chars):
                    chars.remove(s[windowStart])
                    windowStart += 1
                chars.add(currChar)
        
        return maxLength
