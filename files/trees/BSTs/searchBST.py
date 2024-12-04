# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return
        if root.val == val:
            return root
        
        # root val is too small, search on the right side
        if val > root.val:
            return self.searchBST(root.right ,val)
        
        # root val is too big, search on left side
        elif val < root.val:
            return self.searchBST(root.left, val)
