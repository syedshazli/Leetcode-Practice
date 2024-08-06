class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        ans = []
        for i in range(2*n):
            if i <n:
                # if i is less than the length of nums
                ans.append(nums[i])
            else:
                ans.append(nums[i-n])
        return ans
