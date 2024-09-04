class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        #array nums... length of n but have n integers
        # current element is part of [1,n]
        # my brain knows what neess to be done.
        # if i not in nums[i] new.append(i)
        # numbers in range [1,n] that are not in nums
        new = []
        hashmap = dict()
        for i in range(len(nums)):
            hashmap[nums[i]] = nums[i]
        for i in range(1, len(nums)+1):
            if i not in hashmap:
                new.append(i)
        return new
        
