class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numCount = {}
        for num in nums:
            if (num not in numCount):
                numCount[num] = 1
            else:
                numCount[num] += 1
            
            if (numCount[num] > len(nums) // 2):
                return num
        