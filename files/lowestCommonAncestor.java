/**
*Notes
* This was very similar to the leetcode problem that searches for a target within a BST.
* All we really had to change was to say if the root is greater than p and q, search in the left (where all values of BST less than root are on left)
* if the root is less than p and q, search in the right(where all values of BST greater than root are on the right)
* else, return the root.
* This is a DFS implementation
*/


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
        * 
         */

            if(root != null){
            if(root.val>p.val && root.val>q.val){return lowestCommonAncestor(root.left, p, q);}
            else if(root.val<p.val && root.val<q.val){return lowestCommonAncestor(root.right, p, q);}
           
            }
         

return root; 
        

    }
}
