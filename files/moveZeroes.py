#Notes
# I saw the remove and append method looking through W3 schools
# I saw that we can remove the current element if zero, and use append to send the zero to the end of the list
# Maintains order of the other elements!
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
        return nums
