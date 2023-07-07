# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #Base Case - None
        if (root is None):
            return []
        # Base Case - Leaf
        if (root.left is None and root.right is None):
            return [root.val]
        else:
            rightChildView = self.rightSideView(root.right)
            leftChildView = self.rightSideView(root.left)
            return [root.val] + rightChildView + leftChildView[len(rightChildView):]