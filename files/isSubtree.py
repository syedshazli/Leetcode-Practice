#Notes
# Here we have 2 recursive functions. Thinking of the solution wasnt hard but coding it was
# Make a recursive helper function that checks if 2 trees are the same
# In the main function, if the subroot is none, return true, and if the subroot is not none but the main root is, return false
# if the helper function of the subroot and root comes back as true, return true
# else, compare the right of the root compared to the root of the subtree and compare left of root to the root of subtree.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def helper(root, subRoot):
            if root is None and subRoot is None:
                return True
            if root is not None and subRoot is not None and root.val == subRoot.val:
                return helper(root.left, subRoot.left) and helper(root.right, subRoot.right)
            
            return False
            


        # if p.val != q.val and p is not None and q is not None:
        #     return False
        if subRoot is None:
            return True
        if root is None and subRoot is not None:
            return False
        if helper(root, subRoot) == True:
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
