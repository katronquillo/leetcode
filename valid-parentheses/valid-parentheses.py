class Solution:
    """
    Input: string of parentheses
    Output: True iff string is valid (I.E. all parentheses closed)

    Note...
    For every opening bracket, the next closing bracket seen must match

    Algorithm...
    - Add all opening brackets into a stack
    - When closing brackets is encountered...
        - Pop opening bracket from stack
        - Return False if they don't match 
    """
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if (char in ["(", "{", "["]):
                stack.append(char)
            else:
                if (len(stack) == 0):
                    return False
                    
                opening = stack.pop()
                if (not self.isMatching(opening, char)):
                    return False

        return len(stack) == 0

    def isMatching(self, open: str, close: str) -> bool:
        match = {
            "(": ")",
            "{": "}",
            "[": "]"
        }
        return match[open] == close
        
