class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # max 1's = 0
        # current1's
        # for i in range(len(nums)-1):
        #   if nums[i] == 1 and nums[i+1] == 1:
        #       current1's+=1
        #   else:
        #       max1's = max(max1's, current1's)
        # return max 1's
        maxOnes = 0
        currentOnes = 0
        for i in range(len(nums)):
            if  nums[i] == 1:
                currentOnes+=1
            else:
                currentOnes = 0

            maxOnes = max(maxOnes, currentOnes)
        return maxOnes
        
