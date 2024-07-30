# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->
We want to make sure we can check if the left nodes exist for both, and if they do, are they the same value. The same thing can be said for the right nodes. If at our base case, one is none and the other isn't return false. Otherwise return true 

# Approach
Our base cases cover the situation where both nodes are none, or one contains a value and the other doesn't. So then once these are returned, if just one of the cases in the return comes up as False (such as values not being equal), the function returns false as well. So after the base cases, return the recursive solution for right, left and if val's are equal

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


        return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left) and p.val == q.val
