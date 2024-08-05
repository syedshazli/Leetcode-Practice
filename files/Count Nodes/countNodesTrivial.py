# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxVal = 0
        if root is None:
            return 0
        rootRight = self.countNodes(root.right)
        rootLeft =  1 + self.countNodes(root.left)
        maxVal += (rootLeft + rootRight)
        return maxVal
