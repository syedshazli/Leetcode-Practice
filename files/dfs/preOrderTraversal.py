# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        preOrder = []
        def helper(root):
            if root is None:
                return
            preOrder.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return preOrder
