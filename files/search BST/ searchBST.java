/**
* First Binary Search Tree Problem, congratulations
* I felt like this was similar to a binary search.
* If the root value is bigger than the target, call the function again with it's left child which would be smaller
*  Likewise if the root value is smaller than the target, call the function again with it's right child which would be bigger
*  Return root if none of these are true
*  This should all be inside a if(root!= null), after that, return Null which means the target isn't available.

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
    public TreeNode searchBST(TreeNode root, int val) {
        
        if(root != null){
        if(root.val>val){return searchBST(root.left, val);}
        else if(root.val<val){return searchBST(root.right, val);}
        return root;
        }
        return null;
    }
}
