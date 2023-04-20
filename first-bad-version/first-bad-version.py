# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while (left <= right):
            midPoint = (right + left) // 2
            currisBad = isBadVersion(midPoint)

            # Current is Bad
            if (currisBad):
                if ((midPoint == 1) or (midPoint > 1 and not isBadVersion(midPoint - 1))):
                    return midPoint
                else:
                    right = midPoint - 1

            # Current is Good - First bad occurs after this point
            else: 
                left = midPoint + 1

