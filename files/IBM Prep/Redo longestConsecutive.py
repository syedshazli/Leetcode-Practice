class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # find the max number in the list
        # for each number in this range,
        #if current element - 1 not in nums:
            #maximum = max(currentLength, maxLength)
        #   reset counter to 1
        #else, counter +=1, currentLength +=1
        maximum = 1
        j = 0
        hashmap = {}
        if len(nums) == 0:
            return 0
        for i in range(len(nums)):
            hashmap[nums[i]] = 0
        
        for num in hashmap:
            if num-1 in hashmap:
                # issue is that it is checking -1 and -1
                print(nums[i]-1)
                continue
           

                #start of sequence
            j =1 
            while num+j in hashmap:
                j+=1

            maximum = max(maximum, j)
        print(hashmap)
        return maximum
