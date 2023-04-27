class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        
        def twoSum(index: int, target: int) -> List[int]:
            i = nums[index]
            left, right = index + 1, len(nums) - 1

            while (left < len(nums) and right >= 0 and left < right):
                j, k = nums[left], nums[right]
                if (j + k < target):
                    left += 1
                elif (j + k > target):
                    right -= 1
                else:
                    result.append([i, j, k])
                    left += 1
                    right -= 1
                    while (left < right and nums[left] == nums[left - 1]):
                        left += 1
                    while (left < right and nums[right] == nums[right + 1]):
                        right -= 1
        
        for index in range(len(nums)):
            if (index > 0 and nums[index] == nums[index - 1]):
                continue
            else:
                twoSum(index, -nums[index])
        
        return result

        