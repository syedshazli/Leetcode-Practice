#includes a binary search aspect
# required to sort first as done in two sum II
# need to review a lot
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #recommended to do two sum II
        nums.sort()
        correct = []
       
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i + 1
            right = len(nums) -1

            while left < right:
                 #binary search aspect
                 threeSum = nums[left] + nums[right] + nums[i]
                 if threeSum > 0:
                    right -= 1
                 elif threeSum < 0:
                    left += 1
                 else:
                    correct.append([nums[i], nums[left], nums[right] ])
                    left += 1

                    while nums[left] == nums[left - 1] and left < right:
                         left += 1 
                    
        return correct     
