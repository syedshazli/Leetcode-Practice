#Notes
# Thought this would be easy but ended up being a little harder than exoected
# Also thought a bottom up approach would work out
# I wasnt aware that LC let you call your own functions inside the function. I leveraged this shortly after for a DFS function
# We go to the depths of the left and right, updating result if it's greater after we find them (in the DFS function)
# In the dfs function, we return 1 + max(left, right) bcs we are returning the height
# Outside the DFS function, call dfs passing in the root and return result


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        result = [0]

   

        def dfs(root):
            if not root:
                return -1

            left = dfs(root.left)
            right = dfs(root.right) 
            result[0] = max(result[0], 2 + left+right)
        
        #they go depth first and bubble up after. "Bottom up approach"

            return 1 + max(left, right)
        
        dfs(root)
        return result[0]
        
