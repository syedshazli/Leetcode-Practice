#Notes
# Had to add the +1 to len(nums) due to confusing test case
# Python makes it easy by saying if i in range(len(nums)+1) not in nums, return i, 
# else we can return 0
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)+1):
            if i not in nums:
                return i
            
        return 0
