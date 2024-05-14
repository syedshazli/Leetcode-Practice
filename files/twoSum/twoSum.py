class Solution(object):
    def twoSum(self, nums, target):
        correct = [0,0]
        newMap = dict()
        sumVal = 0
        for i in range(len(nums)):
            sumVal = target - nums[i]
            if sumVal in newMap:
                correct[0] = newMap[sumVal]
                correct[1] = i
            newMap[nums[i]] = i 
        return correct



    #
    #
    #
