class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        count = 0
        zerocount = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i] 
                count+=1
                #nums.append(0)
            else: 
                zerocount +=1

        
        for i in range(len(nums)-1, -1, -1):
            if zerocount == 0:
                break
            else:
                nums[i] = 0
                zerocount-=1
           

        return nums
