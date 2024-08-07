# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):

        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
       
        rootRight = 1+ self.maxDepth(root.right)
        rootLeft =  1 + self.maxDepth(root.left)
        maxVal = max(rootRight, rootLeft)
        return maxVal
