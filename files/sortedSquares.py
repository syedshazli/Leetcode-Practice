#Notes
# The sort method in python makes it so much easier
# Just square the elements (or multiply by itslef) for each i in nums
# After you're done with the for loop, sort the array, and return the array
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
            
        nums.sort()
        return nums
