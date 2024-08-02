# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#Notes
# Figured this one out after some help on what a in order traversal actually is
# We would need a helper function to prevent two different return types
# the helper function just returns up if the current root is none, else, we just call helper on the left
#after calling this, we append the current root value. This is because the helper(roo.left) will be done executing once it found a null left value
# After this, we know a left value doesnt exist for the root, so we explore the right side of the root

#Traverse left
#visit node
#traverse right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        inOrder = []
    
        def helper(root):
            if root is None:
                return
                
            helper(root.left)
            inOrder.append(root.val)
            helper(root.right)
        helper(root)

        
        # self.inorderTraversal(root.right)
            
            
        return inOrder
