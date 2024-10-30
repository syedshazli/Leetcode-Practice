class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = hashmap.get(nums[i],0)+1
        
        for key in hashmap:
            if hashmap.get(key)!=2:
                return key
        
        
        
