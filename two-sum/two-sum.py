class Solution:
    """
    Input: array of ints (nums) and int (target)
    Output: Indices of two numbers, x and y, such that x + y = target
    
    Algorithm...
    1. Iterate through each element in the array
    2. Keep track of seen values and their indices in a dictionary 
    3. Look for the pair for each element (y = target - x)
    4. Look in dictionary to find the index of their pair

    Time - O(n)
    Space - O(n)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            currValue = nums[i]
            
            if (currValue in seen):
                seen[currValue].append(i)
            else:
                seen[currValue] = [i]

            reqPair = target - currValue
            if (reqPair in seen and seen[reqPair][0] != i):
                return [i, seen[reqPair][0]]

        return [-1, -1]
            

        