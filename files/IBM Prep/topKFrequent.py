class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #ayoo, this was the Investing Association stock market comp problem
        # we want to see how many times an element shows up (hashmap!)
        # we can sort hashmaps by their values.
        # so then, first make the key the actual number and the value how many times it occurs
        # hashmap.sort()
        #for i in range(k), add nums[i] to list
        resArr = []
        hashmap = dict()
        for w in range(len(nums)):
            hashmap[nums[w]] = hashmap.get(nums[w],0)+1
        
        # when we sort, we also want highest to lowest
        
        #could make a queue, take max value in hashmap, append key to array, and remove from hashmap

        i = 0
        for key in sorted(hashmap, key = hashmap.get, reverse = True):
            maxi = max(hashmap)
            if i<k:
                resArr.append(key)
                i+=1
            else:
                break
        return resArr
        
