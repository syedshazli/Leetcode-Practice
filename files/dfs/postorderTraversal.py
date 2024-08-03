#Notes
# a post order traversal, which means you explore the whole left subtree, then the right subtree, then the root
# Follows a similat pattern where you need a helper function
# Honestly I just followed the steps that were given of left, right, root. so we call helper for left, then right, and once these are returned,
# append to array


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        #left subtree
        #right subtree
        #root
        postOrder = []
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root):
            if root is None:
                return
            helper(root.left)
            helper(root.right)
            postOrder.append(root.val)
            
           

        helper(root)
        return postOrder
