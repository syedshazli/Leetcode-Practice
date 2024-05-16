class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = 0
        dict = {}
        for i in range(len(nums)):
            if nums[i] not in dict:
                dict[nums[i]] = 1 
                
            else:
                dict[nums[i]] += 1

            if(dict.get(nums[i])> len(nums)/2):
                major = nums[i]
                return major
        return 0

       
