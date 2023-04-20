class Solution:
    """
    Input: Array of integers nums, Integer target
    Output: The index of target in the array, otherwise -1 

    Algorithm...
    1. Keep track of two pointers at both ends - Searching portion of array between pointers
    2. Find the midpoint of the left and right pointers
    3. Compare target to the value at the midpoint, and decrease search array depending
    """
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while (left <= right):
            mid = (left + right) // 2
            if (nums[mid] < target):
                left = mid + 1
            elif (nums[mid] > target):
                right = mid - 1
            else:
                return mid 
        return -1


          

