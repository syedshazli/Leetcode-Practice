class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        returnArray = []
        kcount = 0
        j = 0
        #hashmap, key is the number and value is how many times it pops up
        newMap = dict()
        nums.sort()
        for i in range(len(nums)):
            newMap[nums[i]] = newMap.setdefault(nums[i], 0) +1
            #nums.remove(nums[i])
        
        finalMap = sorted(newMap.keys(), key = lambda x: newMap[x], reverse=True)
       
        for key in finalMap:
            if(kcount>=k):
                break
            returnArray.append(key )
            kcount+=1

        #print(newMap)
        return returnArray
        
