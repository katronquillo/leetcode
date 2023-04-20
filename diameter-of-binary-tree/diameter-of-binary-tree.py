# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiameter = [float("-inf")]

        def dfs(root):
            # Base Case - Empty Tree
            if (root is None):
                return (0, -1)

            # Base Case - Leaf
            elif (root.left is None and root.right is None):
                diameter, height = 0, 0
                maxDiameter[0] = max(maxDiameter[0], diameter)
                return (diameter, height)
            
            # Recursive Case - Node with Children
            else:
                leftDiameter, leftHeight = dfs(root.left)
                rightDiameter, rightHeight = dfs(root.right)

                diameter = leftHeight + rightHeight + 2
                height = 1 + max(leftHeight, rightHeight)

                maxDiameter[0] = max(maxDiameter[0], diameter)

                return (diameter, height)

        dfs(root)
        return maxDiameter[0]
        