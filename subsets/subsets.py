class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        powerSet, currSubset = [], []

        def dfs(i: int):
            # Base Case - Index is out of bounds, full subset created
            if (i >= len(nums)):
                powerSet.append(currSubset.copy())
                return
            
            # Choice 1 - Include the element at nums[i] in subset
            currSubset.append(nums[i])
            dfs(i + 1)
            
            # Choice 2 - Do not include the element at nums[i] in subset
            currSubset.pop()
            dfs(i + 1)
        
        dfs(0)
        return powerSet