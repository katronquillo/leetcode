class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in range(len(nums))]

        # Iterate forward in array to get prefix product
        for i in range(1, len(nums)):
            result[i] = result[i - 1] * nums[i - 1]
        
        # Iterate backward in array to get suffix product
        suffixProduct = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffixProduct
            suffixProduct *= nums[i]
            
        return result
