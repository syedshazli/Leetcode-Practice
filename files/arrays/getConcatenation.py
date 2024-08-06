# we can initialize an array of size 2*n, and can reduce runtime by iterating throug length of n
# from there we set values to ans[i] and ans[i+len(nums)] solved!
class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = [0] * (2*n)
    
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        return ans
