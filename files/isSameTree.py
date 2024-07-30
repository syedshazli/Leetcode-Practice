class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        elif p is None and q is not None or p is not None and q is None:
            return False

        # if p.val != q.val and p is not None and q is not None:
        #     return False


        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left) and p.val == q.val
