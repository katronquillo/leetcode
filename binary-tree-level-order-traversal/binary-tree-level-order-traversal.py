# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if (root is None):
            return []

        result = []
        queue = deque()
        queue.append(root)
        while (len(queue) > 0):
            levelLength, level = len(queue), []
            for _ in range(levelLength):
                popped = queue.popleft()

                level.append(popped.val)

                if (popped.left):
                    queue.append(popped.left)
                if (popped.right):
                    queue.append(popped.right)

            result.append(level)
                
        return result
        