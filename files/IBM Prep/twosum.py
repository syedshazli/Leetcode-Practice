class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        resArr = [0,0]
        num = 0
        for i in range(len(nums)):
            numtoFind = target-nums[i]
            #print(numtoFind)
            if numtoFind in hashmap:
                resArr[0] = hashmap[numtoFind]
                resArr[1] = i
                return resArr
            hashmap[nums[i]] = i
