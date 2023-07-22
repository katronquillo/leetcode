# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    - Root is first element in pre-order traversal
    - Left subtree is elements to left of root in in-order
    - Right subtree is elements to right of root in in-order
    - Tree contains unique values
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        else:
            # Create the root node
            rootVal = preorder[0]
            root = TreeNode(rootVal)

            # Find preorder and inorder traversal for left and right subtrees
            rootInOrderIndex = inorder.index(rootVal)
            inorderL, inorderR = inorder[:rootInOrderIndex], inorder[rootInOrderIndex + 1:]

            numLeft = len(inorderL)
            preorderL, preorderR = preorder[1:numLeft + 1], preorder[numLeft + 1:]

            # Build left and right subtrees 
            root.left = self.buildTree(preorderL, inorderL)
            root.right = self.buildTree(preorderR, inorderR)
        
            return root
