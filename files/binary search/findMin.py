class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while low < high:
            middle = (low+high)//2
            if nums[middle]>nums[middle+1]:
                return nums[middle+1]
            if nums[middle-1]>nums[middle]:
                return nums[middle]

            elif nums[middle] > nums[high]:
                low = middle+1
            elif nums[middle]< nums[high]:
                high = middle-1
        return nums[0]
            
        
