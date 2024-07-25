class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        high = len(nums)-1
        low = 0
        
        while high >low:
            
            mid = low + (high-low)/2
            print(mid)
            if nums[mid] < target:
                low=(mid+1)
                #the middle value is too big for our target. adjust the high end to be one less
            elif nums[mid] > target:
                high= (mid-1)
                # the middle value is too small for the target. increase lower bound to 1 more
            else:
                return mid
        return -1
        
