# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    """
    Input: Root of binary tree
    Output: True iff tree is height balanced

    Height Balanced: Depth of subtrees for every node never differs by more than one

    - Recursively check the height of the left and right children
    - Keep track of each node's current height and whether the tree rooted 
    at that node is balanced 
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def isBalanced_Recursive(root):
            if (root is None):
                return (True, 0)
            elif (root.left is None and root.right is None):
                return (True, 1)
            else:
                (leftBalanced, leftHeight) = isBalanced_Recursive(root.left) # [t, 1]
                (rightBalanced, rightHeight) = isBalanced_Recursive(root.right) # [t, 1]

                currBalanced = abs(leftHeight - rightHeight) <= 1
                currHeight = 1 + max(leftHeight, rightHeight)
                if (leftBalanced and rightBalanced):
                    return (currBalanced, currHeight)
                else:
                    return (False, currHeight)
        (rootBalanced, rootHeight) = isBalanced_Recursive(root)
        return rootBalanced
                    



                

