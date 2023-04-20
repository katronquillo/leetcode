class Solution:
    """
    Input: Strs s and t
    Output: True iff t is an anagram of s

    Algorithm...
    1. Maintain a dictionary of characters to occurrences
    2. Iterate through each string and update respective dictionaries

    Time - O(n)
    Space - O(m + n)
    """
    def isAnagram(self, s: str, t: str) -> bool:
        sChars, tChars = {}, {}
        sIndex, tIndex = 0, 0
        while (sIndex < len(s) and tIndex < len(t)):
            currS, currT = s[sIndex], t[tIndex]
            if (currS not in sChars):
                sChars[currS] = 0
            if (currT not in tChars):
                tChars[currT] = 0
            
            sChars[currS] += 1
            tChars[currT] += 1

            sIndex += 1
            tIndex += 1
        
        if (sIndex < len(s) or tIndex < len(t)):
            return False
        
        return sChars == tChars