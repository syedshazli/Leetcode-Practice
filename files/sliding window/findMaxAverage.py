class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        current = sum(nums[:k])
        maxsum= current
   
        for i in range(k, len(nums)):
            #add the number coming in, subtract number coming out
            current += nums[i]-nums[i-k]
            maxsum = max(maxsum, current)
        return maxsum/k
        # if len(nums) == 1:
        #     return nums[0]
        # while k<=len(nums):
        #     temp = nums[added:k]

        #     lex = sum([x for x in temp])
        #     summed = lex/(k-added)

        #     if summed>maxxed:
        #         maxxed =summed
        #         added+=1
        #         k+=1
        #     else:
        #         added +=1
        #         k+=1
        # return maxxed
