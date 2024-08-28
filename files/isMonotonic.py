
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        monoInc = True
        monoDec = True

        # need to have separate checks for monotonic increasing or decreasing
        if len(nums) == 0 or len(nums) ==1:
            return True

        for i in range(1, len(nums)):
            if nums[i-1]>nums[i]:
                print(nums[i])
                monoInc = False
            elif nums[i-1]<nums[i]:
                print(nums[i])
                monoDec = False
            else:
                continue
        
        if monoInc == True or monoDec == True:
            return True
        else:
            return False
            
