class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #let's try to understand what the left and right pointers mean
        #because we will always have our middle to, so in context of middle
        left = 0
        right = len(nums)-1
        lowest = nums[0]
       #not returning how many times we returned, rather the minimum element
        while left <= right:
                #middle is greater than the end element, search in right side
            if nums[left] < nums[right]:
                lowest = min(lowest, nums[left])
                return lowest

            middle = (left+right)/2
            lowest = min(lowest, nums[middle])
            if nums[middle] >= nums[left]:
                left = middle +1
              #we shift left even if its less than middle bc in a sorted array this means anything to the right will be the pivot or lesser value of the array
            else:
                right = middle-1
                
        return lowest
