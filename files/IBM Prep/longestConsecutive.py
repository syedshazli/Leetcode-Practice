class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find the max number in the list
        # for each number in this range,
        #if current element - 1 not in nums:
            #maximum = max(currentLength, maxLength)
        #   reset counter to 1
        #else, counter +=1, currentLength +=1
        maximum = 1
        if(len(nums) == 0):
            return 0
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = 0

        for num in hashmap:
            if num-1 in hashmap:
                continue
            j = 0
            while j+num in hashmap:
                j+=1
            maximum = max(j, maximum)
        return maximum
