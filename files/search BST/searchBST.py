# First Binary Search Tree Problem, congratulations
# I felt like this was similar to a binary search.
# If the root value is bigger than the target, call the function again with it's left child which would be smaller
#  Likewise if the root value is smaller than the target, call the function again with it's right child which would be bigger
#  Return root if none of these are true
#  This should all be inside a if(root!= null), after that, return Null which means the target isn't available.





# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        if(root.val>val):
            return self.searchBST(root.left, val)
        elif root.val<val:
            return self.searchBST(root.right, val)
        return root
        
