
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        
        """
        :type root: TreeNode
        :rtype: bool
        """
        #will just be a DFS implementation, and return if the depth differes by more than one
        #recursice solution
        #use helper function
        def helperFunction(root):
            if root is None:
                return 0
            right = helperFunction(root.right)
            left = helperFunction(root.left)
            if left == -1 or abs(left-right)>1:
                return -1
                #basically just means returning false. If the abs(left-right)>1 happens, 
                #this means we're uneven at some point. Grwater than 2 on some level
            return 1+max(left,right)

        return helperFunction(root) !=-1
