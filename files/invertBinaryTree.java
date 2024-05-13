/**
*Notes on Problem
*My implementation is a Depth First Search (DFS) Approach
*The implementation uses recursion to find the leaf nodes, which then return the parent node to allow swapping
* We switch the left and the right of the roots to ivnert the tree properly
*/


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
    public TreeNode invertTree(TreeNode root) {
    
            if(root == null){return root;}
            TreeNode leftTree = invertTree(root.left);
            TreeNode rightTree = invertTree(root.right);

            root.left = rightTree;
            root.right = leftTree;

            return root;


    }
      
    

}
