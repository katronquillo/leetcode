class Solution {
    /**
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
     */
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0;
        HashSet<Character> windowChars = new HashSet<Character>();

        int windowStart = 0;
        for (int windowEnd = 0; windowEnd < s.length(); windowEnd++) {
            char currChar = s.charAt(windowEnd);
            
            // Character not in current window - Add character + Calculate new window length
            if (!windowChars.contains(currChar)) {
                windowChars.add(currChar);
                int windowLength = (windowEnd - windowStart) + 1;
                maxLength = Math.max(maxLength, windowLength);
            }

            // Chracter in current window - Shrink window to remove duplicate
            else {
                while (windowStart <= windowEnd && windowChars.contains(currChar)) {
                    char startChar = s.charAt(windowStart);
                    windowChars.remove(startChar);
                    windowStart += 1;
                }
                windowChars.add(currChar);
            }          
        }

        return maxLength;
    }
}