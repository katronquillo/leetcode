class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Top-Down DP - dp[i] is True iff s[i:] can be segmented
        dp = [False for _ in range(len(s) + 1)]
        dp[len(s)] = True

        # Iterate from the end of the string and fill table
        for i in range(len(s) - 1, -1, -1):
            # Iterate through all possible substring endings
            for j in range(i + 1, len(s) + 1):
                currWord, currWordLength = s[i:j], len(s[i:j])

                # Check if current substring is in the dictionary
                if (currWord in wordDict and dp[j]):
                    dp[i] = True
                    break

        return dp[0]