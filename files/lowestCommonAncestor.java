/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        /**
        *Thoughts
        * Will probably need to implement DFS and go until node is null as base case ?
        * Compare with other times node is null and find the 
        * Common ancestor means something ABOVE you, and the lowest value of the connected
        * search for the first value that is between p and q. That will be your lowest common ancestor
        * so is this basically a dfs of root, where root.left = p and root.right = q?
         */

            if(root != null){
            if(root.val>p.val){return lowestCommonAncestor(root.right, p, q);}
            else if(root.val<q.val){return lowestCommonAncestor(root.left, p, q);}
            }
           return root; 


        

    }
}
