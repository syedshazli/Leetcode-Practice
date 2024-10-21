class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        maxSize  = 0
        zeroCount  = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount +=1
                
            while zeroCount > 1:
                if nums[left] == 0:
                    zeroCount-=1
                left+=1

            

            maxSize = max(maxSize, right-left)
        return maxSize

        

        
