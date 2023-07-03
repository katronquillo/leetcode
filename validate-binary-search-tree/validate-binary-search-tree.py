# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, minVal, maxVal) -> bool:
            if (root is None):
                return True 
            if (root.left is None and root.right is None):
                return (minVal < root.val < maxVal)
            else:
                isValidLeft = dfs(root.left, minVal, root.val)
                isValidRight = dfs(root.right, root.val, maxVal)
                
                
                return (minVal < root.val < maxVal) and (isValidLeft and isValidRight)
        
        return dfs(root, float("-inf"), float("inf"))