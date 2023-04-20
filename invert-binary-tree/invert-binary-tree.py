# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Input: Root of binary tree
    Output: Root of the inverted binary tree (Switching left and right children)
    """
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        elif root.left is None and root.right is None:
            return root
        else:
            # Invert Children
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)

            return root
        