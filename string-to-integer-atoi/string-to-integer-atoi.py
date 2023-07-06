class Solution:
    """
    - Ignore leading whitespace
    - Check for "-" or "+" -- Determines if positive or negative
        - Assume positive if neither is present
    - Read characters until next non-digit character/end is reached
    - If integer is out of range [-2^31, 2^31 - 1], clamp

    """
    def myAtoi(self, s: str) -> int:
        # Trim whitespace
        s = s.strip()

        # Iterate through each character in the string
        result, sign, beginning = 0, 1, True
        for i in range(len(s)):
            currChar = s[i]
            if beginning: # At the beginning of the string
                if (currChar == "-"):
                    sign = -1
                elif (currChar.isdigit()):
                    result = (result * 10) + int(currChar)
                elif (not currChar.isdigit() and currChar != "+"):
                    break
                beginning = False
            elif (not currChar.isdigit()):
                break
            else:
                result = (result * 10) + int(currChar)
                if (result * sign) > (2**31 - 1):
                    return (2**31 - 1)
                elif (result * sign) < (2**31 * -1):
                    return (2**31 * -1)

        return result * sign
