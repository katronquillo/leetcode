class Solution {
    public int lengthOfLongestSubstring(String s) {
        int maxLength = 0;
        HashSet<Character> chars = new HashSet<Character>();

        int windowStart = 0;
        for (int windowEnd = 0; windowEnd < s.length(); windowEnd++) {
            char currChar = s.charAt(windowEnd);
            
            // Character not in current window - Add character + Calculate new window length
            if (!chars.contains(currChar)) {
                chars.add(currChar);
                int windowLength = (windowEnd - windowStart) + 1;
                maxLength = Math.max(maxLength, windowLength);
            }

            // Chracter in current window - Shrink window to remove duplicate
            else {
                while (windowStart <= windowEnd && chars.contains(currChar)) {
                    char startChar = s.charAt(windowStart);
                    chars.remove(startChar);
                    windowStart += 1;
                }
                chars.add(currChar);
            }          
        }

        return maxLength;
    }
}