class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        resArr = []
 
        #for each number, store current number - target in array
        # if the current number is in the hashmap, add the value of the hashmap to a result array as well as current index
        for i in range(len(nums)):

            if nums[i] in hashmap: #we found the 2nd value
                print(nums[i])
                resArr.append(i)
                resArr.append(hashmap[nums[i]])
                return resArr
            else:
                current = target-nums[i]
                hashmap[current] = i
