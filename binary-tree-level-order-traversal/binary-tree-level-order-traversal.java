/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();

        // Tree is empty
        if (root == null) {
            return result;
        }

        Deque<TreeNode> deque = new ArrayDeque<>();
        deque.addFirst(root);

        while (deque.size() > 0) {
            int levelLength = deque.size();
            List<Integer> currLevel = new ArrayList<Integer>();

            for (int i = 0; i < levelLength; i++) {
                // Add current node to current level
                TreeNode currNode = deque.removeFirst();
                currLevel.add(currNode.val);

                // Add children for next level
                if (currNode.left != null) deque.addLast(currNode.left); 
                if (currNode.right != null) deque.addLast(currNode.right); 
            }
            
            result.add(currLevel);
        }

        return result;
    }
}